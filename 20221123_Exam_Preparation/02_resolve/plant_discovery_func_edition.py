def rate(dictionary, current_plant, current_rating):
    dictionary[current_plant]["rating"].append(current_rating)
    return dictionary


def update(dictionary, current_plant, current_rarity):
    dictionary[current_plant]["rarity"] = current_rarity
    return dictionary


def reset(dictionary, current_plant):
    dictionary[current_plant]['rating'] = []
    return dictionary


plants = int(input())
plant_dictionary = {}
for index in range(plants):
    plant, rarity = input().split("<->")
    if plant in plant_dictionary:
        plant_dictionary[plant]["rarity"] = int(rarity)
    else:
        plant_dictionary[plant] = {"rarity": int(rarity), "rating": []}

while True:
    command = input().split(" - ")
    if command[0] == "Exhibition":
        break

    action, plant = command[0].split(": ")

    if plant not in plant_dictionary.keys():
        print("error")
        continue

    if action == "Rate":
        rating = int(command[1])
        plant_dictionary = rate(plant_dictionary, plant, rating)

    elif action == "Update":
        new_rarity = int(command[1])
        plant_dictionary = update(plant_dictionary, plant, new_rarity)

    elif action == "Reset":
        plant_dictionary = reset(plant_dictionary, plant)

print("Plants for the exhibition:")
for key, value in plant_dictionary.items():
    average_rating = 0
    if plant_dictionary[key]['rating']:
        average_rating = sum(plant_dictionary[key]["rating"]) / len(plant_dictionary[key]['rating'])
    print(f"- {key}; Rarity: {plant_dictionary[key]['rarity']}; Rating: {average_rating:.2f}")

# test inputs:

# 3
# Arnoldii<->4
# Woodii<->7
# Welwitschia<->2
# Rate: Woodii - 10
# Rate: Welwitschia - 7
# Rate: Arnoldii - 3
# Rate: Woodii - 5
# Update: Woodii - 5
# Reset: Arnoldii
# Exhibition

# 2
# Candelabra<->10
# Oahu<->10
# Rate: Oahu - 7
# Rate: Candelabra - 6
# Exhibition
