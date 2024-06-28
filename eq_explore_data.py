import json

filename = 'eq_data_1_day_m1.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'eq_data_1_day_m1.geojson'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
