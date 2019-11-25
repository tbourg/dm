import csv
import folium



data = []
with open('dataset/data.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        row = dict(row)
        data.append(row)
#print(data)

folium_map = folium.Map(location=[40.7, -74],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")
for ride in data:
    print(ride)
    marker = folium.CircleMarker(location=[float(ride['pickup_latitude']), float(ride['pickup_longitude'])], radius=2)
    marker = folium.CircleMarker(location=[float(ride['dropoff_latitude']), float(ride['dropoff_longitude'])], radius=2)
    marker.add_to(folium_map)
folium_map.save("my_map.html")
