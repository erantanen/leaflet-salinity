

import os
import pandas as pd
import csv
import pre_proc_depth_id as pre

def open_csv(proc_file):
    # data = pre.data_to_proc(proc_file, proc_fields)
    # this is the consolidated csv just read each line
    data_b = os.path.join(os.getcwd(), "input", proc_file)
    return pd.read_csv(data_b)


# fields = ['date', 'lat', 'long', 'Depthm', 'T_degC', 'Salnty']
csv_data_new = open_csv("data_everything.csv")




df_2016 = csv_data_new

df_2016.head(5)


lat_1 = 30
lat_2 = 33
lon_1 = -122
lon_2 = -120
cond_1a = df_2016.lat.between(lat_1,lat_2)
cond_1b = df_2016.long.between(lon_1,lon_2)
cond_2 = df_2016.date.str.startswith("1949")
cond_3 = (df_2016.Depthm.notnull() & df_2016.T_degC.notnull())
result_1 = df_2016.loc[ cond_1a & cond_1b & cond_2 & cond_3]
result_1.info()