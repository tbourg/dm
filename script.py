import numpy as np
import pandas as pd
import sklearn
import sklearn.cluster
import folium
import requests
import ast

with open('api.txt') as f:
    api = f.readline()
print(api)
url_format = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{},{}.json?access_token=' + api
poi_txt = []


#data = pd.read_csv('dataset/data.csv')
#print(data.shape)
#data_clr = data[data.passenger_count != 0]
#data_clr = data_clr[39 < data_clr.pickup_latitude]
#data_clr = data_clr[data_clr.pickup_latitude < 42]
#data_clr = data_clr[39 < data_clr.dropoff_latitude]
#data_clr = data_clr[data_clr.dropoff_latitude < 42]
#data_clr = data_clr[-76 < data_clr.pickup_longitude]
#data_clr = data_clr[data_clr.pickup_longitude < -72]
#data_clr = data_clr[-76 < data_clr.dropoff_longitude]
#data_clr = data_clr[data_clr.dropoff_longitude < -72]
#print(type(data_clr))
#print(data_clr.shape)
#pickup = data_clr.filter(like='pickup_l', axis=1)
#print(pickup.shape)
#print(pickup.head(3))
#dropoff = data_clr.filter(like='dropoff_l', axis=1)
#print(dropoff.head(3))
#pickup_clusters = sklearn.cluster.KMeans(n_clusters=30).fit(pickup.to_numpy())
#print(pickup_clusters.cluster_centers_)
with open('dataset/pickup_poi_list.txt') as f:
    data_raw = [s.split() for s in ''.join(f.readlines()).split('\n')]
    data = [[''.join(c for c in s if c not in '[]') for s in row] for row in data_raw]
    data = [[float(e) for e in r if e != ''] for r in data]
data = np.asarray(data)
folium_map = folium.Map(location=[40.7, -74],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")
for poi in data:
    url = url_format.format(poi[0], poi[1])
    print(url)
    r = requests.get(url)
    print(r.json())
    if r.json()['features']:
        poi_txt.append(r.json()['features'][0]['place_name'])
    marker = folium.CircleMarker(location=[poi[1], poi[0]], radius=2, color='red')
    marker.add_to(folium_map)
print(folium_map)
folium_map.save("my_map.html")
print(poi_txt)
with open('dataset/pickup_poi.txt', 'w+') as of:
    of.write('\n'.join(poi_txt))