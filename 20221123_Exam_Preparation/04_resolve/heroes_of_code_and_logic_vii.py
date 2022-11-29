heroes_count = int(input())
heroes_dictionary = {}

for hero in range(heroes_count):
    hero_name, hp, mp = input().split()
    heroes_dictionary[hero_name] = {"hp": int(hp), "mp": int(mp)}

while True:

    command = input()
    if command == "End":
        for hero in heroes_dictionary.keys():
            print(f"{hero}\n  HP: {heroes_dictionary[hero]['hp']}\n  MP: {heroes_dictionary[hero]['mp']}")
        break

    command = command.split(" - ")
    action = command[0]
    hero_name = command[1]

    if action == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes_dictionary[hero_name]["mp"] >= mp_needed:
            heroes_dictionary[hero_name]["mp"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dictionary[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        if heroes_dictionary[hero_name]["hp"] <= damage:
            del heroes_dictionary[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            heroes_dictionary[hero_name]["hp"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dictionary[hero_name]['hp']} HP left!")

    elif action == "Recharge":
        amount = int(command[2])
        if heroes_dictionary[hero_name]['mp'] + amount > 200:
            recharge = 200 - heroes_dictionary[hero_name]['mp']
            heroes_dictionary[hero_name]['mp'] = 200
            print(f"{hero_name} recharged for {recharge} MP!")
        else:
            heroes_dictionary[hero_name]['mp'] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif action == "Heal":
        amount = int(command[2])
        if heroes_dictionary[hero_name]['hp'] + amount > 100:
            recharge = 100 - heroes_dictionary[hero_name]['hp']
            heroes_dictionary[hero_name]['hp'] = 100
            print(f"{hero_name} healed for {recharge} HP!")
        else:
            heroes_dictionary[hero_name]['hp'] += amount
            print(f"{hero_name} healed for {amount} HP!")

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
