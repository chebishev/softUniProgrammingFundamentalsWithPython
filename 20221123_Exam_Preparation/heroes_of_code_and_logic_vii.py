initial_heroes = int(input())
heroes_dictionary = {}

for index in range(initial_heroes):
    hero_name, health_points, mana_points = input().split()

    heroes_dictionary[hero_name] = [int(health_points), int(mana_points)]  # max 100 hp and 200 mp

while True:

    command = input()
    if command == "End":

        break

    command = command.split(" - ")
    action = command[0]
    hero_name = command[1]

    if action == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if mp_needed > heroes_dictionary[hero_name][1]:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            heroes_dictionary[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dictionary[hero_name][1]} MP!")

    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        if damage < heroes_dictionary[hero_name][0]:
            heroes_dictionary[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dictionary[hero_name][0]} HP left!")
        else:
            del heroes_dictionary[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif action == "Recharge":
        amount = int(command[2])
        if heroes_dictionary[hero_name][1] + amount > 200:
            difference = 200 - heroes_dictionary[hero_name][1]
            print(f"{hero_name} recharged for {difference} MP!")
            heroes_dictionary[hero_name][1] = 200
        else:
            print(f"{hero_name} recharged for {amount} MP!")
            heroes_dictionary[hero_name][1] += amount

    elif action == "Heal":
        amount = int(command[2])
        if heroes_dictionary[hero_name][0] + amount > 100:
            difference = 100 - heroes_dictionary[hero_name][0]
            print(f"{hero_name} healed for {difference} HP!")
            heroes_dictionary[hero_name][0] = 100
        else:
            print(f"{hero_name} healed for {amount} HP!")
            heroes_dictionary[hero_name][0] += amount

for hero in heroes_dictionary.keys():
    print(f"{hero}\n  HP: {heroes_dictionary[hero][0]}\n  MP: {heroes_dictionary[hero][1]}")

# test inputs:

# 2
# Solmyr 85 120
# Kyrre 99 50
# Heal - Solmyr - 10
# Recharge - Solmyr - 50
# TakeDamage - Kyrre - 66 - Orc
# CastSpell - Kyrre - 15 - ViewEarth
# End

# 4
# Adela 90 150
# SirMullich 70 40
# Ivor 1 111
# Tyris 94 61
# Heal - SirMullich - 50
# Recharge - Adela - 100
# CastSpell - Tyris - 1000 - Fireball
# TakeDamage - Tyris - 99 - Fireball
# TakeDamage - Ivor - 3 - Mosquito
# End
