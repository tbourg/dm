import csv
import folium
import json
import numpy as np



data = []
lat = []
lon = []
with open('dataset/data.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        row = dict(row)
        if float(row['passenger_count']) != 0 and float(row['pickup_latitude']) != 0 and float(row['dropoff_latitude']) != 0 and float(row['pickup_longitude']) != 0 and float(row['dropoff_longitude']) != 0:
            print(row)
            lat.append(float(row['pickup_latitude']))
            lat.append(float(row['dropoff_latitude']))
            lon.append(float(row['pickup_longitude']))
            lon.append(float(row['dropoff_longitude']))
            data.append(row)
lat = np.ma.masked_outside(np.asarray(lat), 39, 42)
lon = np.asarray(lon)
print(lat)
print(np.amin(lat), np.amax(lat))
#print(data)
'''
folium_map = folium.Map(location=[40.7, -74],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")
for ride in data:
    if float(ride['passenger_count']) != 0:
        print(ride)
        marker = folium.CircleMarker(location=[float(ride['pickup_latitude']), float(ride['pickup_longitude'])], radius=, color='red')
        marker = folium.CircleMarker(location=[float(ride['dropoff_latitude']), float(ride['dropoff_longitude'])], radius=1, color='green')
        marker.add_to(folium_map)
folium_map.save("my_map.html")
'''