import re

map_places = input()
locations_pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
travel_points = 0
valid_locations = re.findall(locations_pattern, map_places)
locations = []
for location in valid_locations:
    locations.append(location[1])
    travel_points += len(location[1])

print(f"Destinations: {', '.join(locations)}")
print(f"Travel Points: {travel_points}")

# test inputs:

# =Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=

# ThisIs some InvalidInput
