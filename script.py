from config import *


def pickup_clustering():
    pickup = data_clr.filter(like='pickup_l', axis=1)
    print(pickup.shape)
    print(pickup.head(3))
    pickup_clusters = sklearn.cluster.KMeans(n_clusters=30).fit(pickup.to_numpy())
    print(pickup_clusters.cluster_centers_)
    data = pickup_clusters.cluster_centers_
    data = np.asarray(data)
    poi_txt = []
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
    folium_map.save(out_dir + "pickup_map.html")
    print(poi_txt)
    with open(out_dir + 'pickup_poi.txt', 'w+') as of:
        of.write('\n'.join(poi_txt))


def dropoff_clustering():
    dropoff = data_clr.filter(like='dropoff_l', axis=1)
    print(dropoff.shape)
    print(dropoff.head(3))
    dropoff_clusters = sklearn.cluster.KMeans(n_clusters=30).fit(dropoff.to_numpy())
    print(dropoff_clusters.cluster_centers_)
    data = dropoff_clusters.cluster_centers_
    data = np.asarray(data)
    poi_txt = []
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
    folium_map.save(out_dir + "dropoff_map.html")
    print(poi_txt)
    with open(out_dir + 'dropoff_poi.txt', 'w+') as of:
        of.write('\n'.join(poi_txt))


def biclustering():
    data = data_clr.filter(items=['dist','fare_amount'])
    print(data.head(3))
    biclusters = sklearn.cluster.SpectralCoclustering(n_clusters=1).fit([[(1,1),(1,1)],[(1,1),(1,1)]])


biclustering()