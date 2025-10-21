from pathlib import Path
import json

#read data s a string and convert to a python object 

path = Path('eq_data/eq_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#extract the list of earthquake features
all_eq_dicts = all_eq_data["features"]
print(f"Number of earthquakes: {len(all_eq_dicts)}")

mags , lats, lons= [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lat = eq_dict["geometry"]["coordinates"][1]
    lon = eq_dict["geometry"]["coordinates"][0]
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)

print(mags[:10])  # Print the first 10 magnitudes for verification
print(lats[:10])    # Print the first 10 latitudes for verification
print(lons[:10])    # Print the first 10 longitudes for verification 
