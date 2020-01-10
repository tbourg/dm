import numpy as np
import pandas as pd
import sklearn
import sklearn.cluster
import folium
import requests
import ast
import os
print(os.getcwd())
import math

def distance(origin, destination):
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d



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
data_clr.insert(0,'dist',[distance((x1,y1),(x2,y2)) for x1,y1,x2,y2 in zip(data_clr.dropoff_latitude, data_clr.dropoff_longitude,data_clr.pickup_latitude, data_clr.pickup_longitude)])
print(type(data_clr))
print(data_clr.shape)