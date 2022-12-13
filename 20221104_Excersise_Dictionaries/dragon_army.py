dragon_dictionary = {}

dragons_count = int(input())

for index in range(dragons_count):
    type, name, damage, health, armor = input().split()

    if type not in dragon_dictionary.keys():
        dragon_dictionary[type] = {}
        if name not in dragon_dictionary[type].keys():
            dragon_dictionary[type] = {name: []}
    else:
        dragon_dictionary[type][name] = []
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    dragon_dictionary[type][name] = [int(damage), int(health), int(armor)]

for type in dragon_dictionary.keys():
    avg_damage, avg_health, avg_armor = 0, 0, 0
    dragons_count = len(dragon_dictionary[type].keys())
    for name in dragon_dictionary[type].keys():
        avg_damage += dragon_dictionary[type][name][0]
        avg_health += dragon_dictionary[type][name][1]
        avg_armor += dragon_dictionary[type][name][2]
    avg_damage /= dragons_count
    avg_health /= dragons_count
    avg_armor /= dragons_count
    print(f"{type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    for name in sorted(dragon_dictionary[type].keys()):
        print(f"-{name} -> damage: {dragon_dictionary[type][name][0]}, health: {dragon_dictionary[type][name][1]}, "
            f"armor: {dragon_dictionary[type][name][2]}")

# test inputs:

# 5
# Red Bazgargal 100 2500 25
# Black Dargonax 200 3500 18
# Red Obsidion 220 2200 35
# Blue Kerizsa 60 2100 20
# Blue Algordox 65 1800 50

# 4
# Gold Zzazx null 1000 10
# Gold Traxx 500 null 0
# Gold Xaarxx 250 1000 null
# Gold Ardrax 100 1055 50
