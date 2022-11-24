countries = input().split(", ")
capitals = input().split(", ")
capitals_dictionary = dict(zip(countries, capitals))
[print(f"{country} -> {capital}") for (country, capital) in capitals_dictionary.items()]

# test inputs:

# Bulgaria, Romania, Germany, England
# Sofia, Bucharest, Berlin, London

# Bulgaria, Germany, France
# Varna, Frankfurt, Paris
