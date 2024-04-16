# leaflet-salinity


This is a continuation of the salinity/temp project there are some
- pre-processing steps previously completed
- this exercise is a narrow focus proof of concept (Coast of Oregon)
- data is to be integrated into a  (https://github.com/Raruto/leaflet-elevation)
- 

Two files are created 
- track<some number>.csv
- track<some number>.gpx

example of .csv
```angular2html
lat,lon,elev
40,-135.0,-4144
40,-134.99,-4128
40,-134.98000000000002,-4093
40,-134.97000000000003,-3928
40,-134.96000000000004,-3970
40,-134.95000000000005,-3974
40,-134.94000000000005,-3910
40,-134.93000000000006,-3895
40,-134.92000000000007,-3749
40,-134.91000000000008,-3645

```

example of .gpx
```angular2html
<?xml version="1.0" encoding="UTF-8"?>
<gpx xmlns="http://www.topografix.com/GPX/1/1" 
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
     xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd" 
     version="1.1" creator="gpx.py -- https://github.com/tkrajina/gpxpy">
  <trk>
    <trkseg>
      <trkpt lat="40" lon="-135.0">
        <ele>-4144</ele>
      </trkpt>
      <trkpt lat="40" lon="-134.99">
        <ele>-4128</ele>
      </trkpt>
      <trkpt lat="40" lon="-134.98000000000002">
        <ele>-4093</ele>
      </trkpt>
      <trkpt lat="40" lon="-134.97000000000003">
        <ele>-3928</ele>
      </trkpt>
      <trkpt lat="40" lon="-134.96000000000004">
        <ele>-3970</ele>
      </trkpt>
      <trkpt lat="40" lon="-134.95000000000005">
        <ele>-3974</ele>
      </trkpt>
      <trkpt lat="40" lon="-134.94000000000003">
        <ele>-3910</ele>
      </trkpt>
```