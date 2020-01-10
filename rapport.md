# Data Mining
## Projet 2019-2020

-----------------------------------------
### Choix du sujet

Nous avons choisi de travailler sur les courses de taxis dans la ville de New York.
L'objectif était de regrouper les courses selon leurs points de départ/d'arrivée pour trouver les lieux les plus souvent desservis par les taxis.
Ces lieux serait alors des lieux remarquables comme des endroits touristiques ou encore des gares et des aéroports. 
Nous pourrions donc identifier les lieux les plus visités.
Cela représente plusieurs intérêts pour quelqu'un qui est nouveau à New York : 
- Savoir quels lieux sont probablement intéressants à visiter.
- Savoir d'où il est probablement facile de trouver un taxi.

### Transformations
Nous avons dans un premier temps nettoyé les données, c'est-à-dire supprimer les enregistrements erronés ainsi que ceux ne nous intéressant pas (coordonnées invalides, nombre de passager égal à zéro, ...).
Puis nous nous sommes focalisés sur trois transformations autour des coordonnées géographiques:
- Réaliser un clustering des points de départs des courses
- Réaliser un clustering des points de dépôt
- Associer un tarif à une distance

### Résultats
#### Clustering points de départ
<iframe src='results/pickup_poi.txt' width='80%' height='800'>
</iframe>
<iframe src='results/pickup_map.html' width='80%' height='800'>
</iframe>

#### Clustering points d'arrivée
<iframe src='results/dropoff_poi.txt' width='80%' height='800'>
</iframe>
<iframe src='results/dropoff_map.html' width='80%' height='800'>
</iframe>

#### Biclustering


--------------------------------------
T.Bourg & T.Buttez - M2IA - UCBL