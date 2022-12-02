import re

string = input()
pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
travel_points = ""
destinations = []
search_pattern = re.findall(pattern, string)
for destination in search_pattern:
    destinations.append(destination[1])  # appending destinations to list, which will be printed at the final
    travel_points += destination[1]  # adding all destinations in order to check the length of the string at the final
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {len(travel_points)}")

# test inputs:

# =Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=

# ThisIs some InvalidInput
