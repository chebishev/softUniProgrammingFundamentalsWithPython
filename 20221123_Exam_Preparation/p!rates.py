command = input()
pirate_dictionary = {}
while command != "Sail":

    city, population, gold = command.split("||")
    if city not in pirate_dictionary.keys():
        pirate_dictionary[city] = {"population": 0, "gold": 0}
    pirate_dictionary[city]["population"] += int(population)
    pirate_dictionary[city]["gold"] += int(gold)

    command = input()

while True:

    command = input().split("=>")
    if command[0] == "End":
        break

    elif command[0] == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        pirate_dictionary[town]["population"] -= int(people)
        pirate_dictionary[town]["gold"] -= int(gold)
        print(f"{town} plundered! {int(gold)} gold stolen, {int(people)} citizens killed.")
        if pirate_dictionary[town]["population"] == 0 or \
                pirate_dictionary[town]["gold"] == 0:
            print(f"{town} has been wiped off the map!")
            pirate_dictionary.pop(town)

    elif command[0] == "Prosper":
        town = command[1]
        gold = int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        pirate_dictionary[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {pirate_dictionary[town]['gold']} gold.")

if pirate_dictionary.keys():
    print(f"Ahoy, Captain! There are {len(pirate_dictionary.keys())} wealthy settlements to go to:")
    for town, values in pirate_dictionary.items():
        print(f"{town} -> Population: {pirate_dictionary[town]['population']} citizens, Gold: {pirate_dictionary[town]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

# test inputs:

# Tortuga||345000||1250
# Santo Domingo||240000||630
# Havana||410000||1100
# Sail
# Plunder=>Tortuga=>75000=>380
# Prosper=>Santo Domingo=>180
# End

# Nassau||95000||1000
# San Juan||930000||1250
# Campeche||270000||690
# Port Royal||320000||1000
# Port Royal||100000||2000
# Sail
# Prosper=>Port Royal=>-200
# Plunder=>Nassau=>94000=>750
# Plunder=>Nassau=>1000=>150
# Plunder=>Campeche=>150000=>690
# End
