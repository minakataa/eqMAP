#************************************************
#****Show the last 100 earthquakes near Japan****
#************************************************
import requests
import folium
import numpy as np
#URL
url = 'https://api.p2pquake.net/v2/history?codes=551&limit=100'
#import data 
p2pquake_json = requests.get(url).json()
df = []
for i in range(1,100):
  Eq_name = p2pquake_json[i]["earthquake"]["hypocenter"]["name"]
  Eq_lat = p2pquake_json[i]["earthquake"]["hypocenter"]["latitude"]
  Eq_lon = p2pquake_json[i]["earthquake"]["hypocenter"]["longitude"]
  Eq_mag = p2pquake_json[i]["earthquake"]["hypocenter"]["magnitude"]
  df.append([Eq_name,Eq_lat,Eq_lon,Eq_mag])


# map size
folium_figure = folium.Figure(width=800, height=700)

# center coordinate
center_lat=35
center_lon=135
folium_map = folium.Map([center_lat,center_lon],zoom_start=4.5).add_to(folium_figure)

# for all ivent
for i in range(0,len(df)):
  folium.CircleMarker(
    location=[df[i][1],df[i][2]],
    radius=((np.e)**(0.6*(df[i][3])-2.9))*10,
    color='#ff0000',
    fill_color='#ff0000',
    icon=folium.Icon(icon="arrows-alt-h")
  ).add_to(folium_map)
folium_map
