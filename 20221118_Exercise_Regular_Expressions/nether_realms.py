import re

demons = input().split(",")  # the names can have extra spaces
demons_stats = {}
health_pattern = r"[^0-9\+\-\*\/\.]"
damage_pattern = r"(\+|\-*[\d]+(\.[\d]+)*)"
damage_operators = r"[\*\/]"

for demon in demons:
    demon = demon.strip()  # if there are extra spaces
    name = re.findall(health_pattern, demon)
    demon_name = ""
    demon_health = 0
    for letter in name:
        demon_name += letter
        demon_health += ord(letter)

    if demon not in demons_stats.keys():
        demons_stats[demon] = []
    demons_stats[demon].append(demon_health)

    damage = re.findall(damage_pattern, demon)
    damage_operations = re.findall(damage_operators, demon)
    demon_damage = 0
    if damage:
        for number in damage:
            demon_damage += float(number[0])
        if damage_operations:
            for operation in damage_operations:
                if operation == "*":
                    demon_damage *= 2
                else:
                    demon_damage /= 2
    demons_stats[demon].append(demon_damage)

for key in sorted(demons_stats):
    print(f"{key.strip()} - {demons_stats[key][0]} health, {demons_stats[key][1]:.2f} damage")

# test inputs:

# M3ph-0.5s-0.5t0.0**

# M3ph1st0**, Azazel

# Gos/ho
