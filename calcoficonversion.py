import numpy as np


def invmercator(mercatorLat, iterations=3):
    mercatorLat = np.array(mercatorLat, dtype='float')
    approxLat = mercatorLat
    for i in range(iterations):
        approxLat = 2 * (np.arctan(np.exp(np.deg2rad(mercatorLat) +
            0.00676866 * np.sin(np.deg2rad(approxLat)))) * 180 / np.pi
            - 45)
    return(approxLat)


def tomercator(latitude):
    latitude = np.array(latitude)
    y = np.rad2deg(np.log(np.tan(np.deg2rad(45 + latitude / 2))) -
        0.00676866 * np.sin(np.deg2rad(latitude)))
    return(y)


def stationtolatlon(x, y=None):
    """
    x is line, y is station, or x is a matrix
    x and y are numbers, lists, tuples, or numpy arrays,
    """
    if y == None:
        line = x[:, 0]
        station = x[:, 1]
    else:
        line = x
        station = y
    
    line = np.array(line, dtype='float')
    station = np.array(station, dtype='float')
    
    # need reshape b/c single numbers could be wrapped in arrays
    if len(line.shape) == 0:
        line = line.reshape(1)
    
    if len(station.shape) == 0:
        station = station.reshape(1)
    
    refLatitude = 34.15 - 0.2 * (line - 80) * np.cos(np.deg2rad(30))
    latitude = refLatitude - (station - 60) * np.sin(np.deg2rad(30)) / 15
    L1 = (tomercator(latitude) - tomercator(34.15)) * np.tan(np.deg2rad(30))
    L2 = (((tomercator(refLatitude) - tomercator(latitude)) /
          (np.cos(np.deg2rad(30)) * np.sin(np.deg2rad(30)))))
    longitude = -1 * (L1 + L2 + 121.15)
    ans = np.vstack((longitude, latitude)).T
    if len(line) == 1:
        ans = ans[0]
    return(ans)


def latlontostation(x, y=None):
    """
    x and y are numbers, lists, tuples, or numpy arrays,
    x can be a matrix with y = None
    """
    if y == None:
        lon = x[:, 0]
        lat = x[:, 1]
    else:
        lon = x
        lat = y
    lon = np.array(lon, dtype='float')
    lat = np.array(lat, dtype='float')
    # need reshape b/c single numbers could be wrapped in arrays
    if len(lon.shape) == 0:
        lon = lon.reshape(1)
    if len(lat.shape) == 0:
        lat = lat.reshape(1)
    # assume we're in the western hemispere
    lon[lon > 180] = -1 * (lon[lon > 180] - 360)
    lon[lon < 0] = lon[lon < 0] * -1
    L1 = (tomercator(lat) - tomercator(34.15)) * np.tan(np.deg2rad(30))
    L2 = lon - L1 - 121.15
    mercRefLatitude = (L2 * np.cos(np.deg2rad(30)) * np.sin(np.deg2rad(30)) +
        tomercator(lat))
    refLatitude = invmercator(mercRefLatitude)
    line = 80 - (refLatitude - 34.15) * 5 / np.cos(np.deg2rad(30))
    station = 60 + (refLatitude - lat) * 15 / np.sin(np.deg2rad(30))
    ans = np.vstack((line, station)).T
    if len(line) == 1:
        ans = ans[0]
    return(ans)

