import numpy as np
import pandas as pd
import sklearn
import sklearn.cluster
import folium
import requests
import ast
import os
print(os.getcwd())

with open('./config/api.txt') as f:
    api = f.readline()
url_format = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{},{}.json?access_token=' + api
in_loc = './dataset/data.csv'
out_dir = './results/'
data = pd.read_csv(in_loc)
print(data.shape)
data_clr = data[data.passenger_count != 0]
data_clr = data_clr[39 < data_clr.pickup_latitude]
data_clr = data_clr[data_clr.pickup_latitude < 42]
data_clr = data_clr[39 < data_clr.dropoff_latitude]
data_clr = data_clr[data_clr.dropoff_latitude < 42]
data_clr = data_clr[-76 < data_clr.pickup_longitude]
data_clr = data_clr[data_clr.pickup_longitude < -72]
data_clr = data_clr[-76 < data_clr.dropoff_longitude]
data_clr = data_clr[data_clr.dropoff_longitude < -72]
print(type(data_clr))
print(data_clr.shape)
