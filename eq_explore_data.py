import json

filename = 'eq_data_1_day_m1.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(len(all_eq_dicts))
print(f'\033[31m{mags[:10]}\n\033[0m'
      f'\033[32m{lons[:5]}\n\033[0m'
      f'\033[33m{lats[:5]}\033[0m')


readable_file = 'readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
