from pathlib import Path
import json
import plotly.express as px


path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#extract the list of earthquake features
all_eq_dicts = all_eq_data["features"]
print(f"Number of earthquakes: {len(all_eq_dicts)}")

mags , lats, lons, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lat = eq_dict["geometry"]["coordinates"][1]
    lon = eq_dict["geometry"]["coordinates"][0]
    title = eq_dict["properties"]["title"]
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)
    eq_titles.append(title)


title = "Global Earthquakes" 
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale="agsunset",
                     labels={'color':'Magnitude'},
                     projection="natural earth",
                     hover_name=eq_titles,
)
fig.show()