initial_plants = int(input())
plant_dictionary = {}
for string in range(initial_plants):

    plant, rarity = input().split("<->")
    if plant not in plant_dictionary.keys():
        plant_dictionary[plant] = {}
    plant_dictionary[plant]["rarity"] = int(rarity)
    plant_dictionary[plant]["rating"] = []

while True:

    command = input()
    if command == "Exhibition":
        print(f"Plants for the exhibition:")
        break

    command = command.split(": ")
    action = command[0]
    stats = command[1]
    stats = stats.split(" - ")
    plant = stats[0]
    if plant not in plant_dictionary.keys():
        print("error")
        continue

    if action == "Rate":
        rating = int(stats[1])
        if "rating" not in plant_dictionary[plant].keys():
            plant_dictionary[plant]["rating"] = rating
        plant_dictionary[plant]["rating"].append(rating)

    elif action == "Update":
        new_rarity = int(stats[1])
        plant_dictionary[plant]["rarity"] = new_rarity

    elif action == "Reset":
        plant_dictionary[plant]["rating"] = []

for key, value in plant_dictionary.items():
    total_rating = sum(plant_dictionary[key]['rating'])
    list_length = len(plant_dictionary[key]['rating'])
    average_rating = 0
    if list_length != 0:
        average_rating = total_rating / list_length
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
