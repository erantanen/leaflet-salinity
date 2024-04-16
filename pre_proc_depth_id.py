#
#
#


import os
import pandas as pd
import csv

# Library based on
# https://swfsc-publications.fisheries.noaa.gov/publications/CR/2013/2013Weber2.pdf
import calcoficonversion as coord

#
# data is pulled from
# https://calcofi.org/data/oceanographic-data/bottle-database/
# current data is from 1949 to 2016 and is approx 680k records/rows x 70 columns
proc_file = "bottle.csv"
#
#

new_csv = 'data_everything.csv'


def cvs_builder(new_csv):
    # standardized csv for all new files
    # newline='' takes out the extra-line
    fh = open(new_csv, 'w', newline='')
    writer = csv.writer(fh)
    # format for usable csv
    # all the csv's should be this struck - so hard coded
    csv_header = ['date', 'lat', 'long', 'Depthm', 'T_degC', 'Salnty']
    writer.writerow(csv_header)
    return writer, fh


def data_to_proc(proc_file, fields):
    # opening up data file for reading
    # dumping into dataframe
    data_b = os.path.join(os.getcwd(), "input", proc_file)
    # we already know the data struct so this is kind of a hard code
    # fields = ['Sta_ID', 'Depth_ID', 'Depthm', 'T_degC', 'Salnty']
    data = pd.read_csv(data_b, usecols=fields)
    return data


def date_builder(row_data_string):
    # format  for contents of Depth_ID
    # (original) 19-4903CR-HY-060-0930-05400560-0000A-3
    # century| - year|month|shipcode|-casttype|Julianday|-casttime|-line station
    # 19     | - 49  | 09  | CR     | - HY    | - 258   | - 0836  | - 0920 0880
    # list - ['19', '4909CR', 'HY', '258', '0836', '09200880', '0048A', '3']

    # string_list = row_data['Depth_ID'].split("-")
    string_list = row_data_string.split("-")
    # cat of 1949
    date_year = string_list[0] + string_list[1][0:2]
    # cat of year and month with dash 1949-09
    # it works - not pretty
    # print(string_list[1][2:4])
    date_month: object = string_list[1][2:4]
    # print(date_month)
    date_with_month = date_year + "-" + date_month
    return date_with_month


def convert_pos(row_data):
    # pulling station id - a conversion is done
    # this gives a lat/long
    lat, long = row_data['Sta_ID'].split(" ")
    long_c, lat_c = coord.stationtolatlon(lat, long)
    return long_c, lat_c


# structure of data_list
fields_old = ['Sta_ID', 'Depth_ID', 'Depthm', 'T_degC', 'Salnty']
proc_file = "bottle.csv"
new_csv = 'data_everything'

data_list = []

# data_b = os.path.join(os.getcwd(), "input", proc_file)
data = data_to_proc(proc_file, fields_old)

# for everything putting this into input for later use
new_csv = os.path.join(os.getcwd(), "input", new_csv + '.csv')
writer, fh_new = cvs_builder(new_csv)

#
#
#

for i, row in data.iterrows():
# for i, row in data.head(1000).iterrows():
    # if for date?

    lat_c, long_c = convert_pos(row)
    data_list = [date_builder(row['Depth_ID']), long_c, lat_c, row['Depthm'], row['T_degC'], row['Salnty']]
    writer.writerow(data_list)

fh_new.close()
