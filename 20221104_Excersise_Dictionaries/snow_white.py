dwarf_dictionary = {}

while True:

    command = input()
    if command == "Once upon a time":
        break

    name, color, physics = command.split(" <:> ")
    physics = int(physics)

    if color not in dwarf_dictionary.keys():
        dwarf_dictionary[color] = {name: physics}
    if name in dwarf_dictionary[color].keys():
        if physics > dwarf_dictionary[color][name]:
            dwarf_dictionary[color][name] = physics

for color in sorted(dwarf_dictionary, key=lambda color: len(dwarf_dictionary[color]), reverse=True):
    for dwarf, physics in sorted(dwarf_dictionary[color].items(), key= lambda x: -(x[1]), reverse=True):
        print(dwarf, physics)


# 10/100

# test inputs:

# Peter <:> Red <:> 2000
# Teodor <:> Blue <:> 1000
# George <:> Green <:> 1000
# Simon <:> Yellow <:> 4500
# Dopey <:> Simon <:> 1000
# Once upon a time

# Grumpy <:> Red <:> 5000
# Grumpy <:> Blue <:> 10000
# Grumpy <:> Red <:> 10000
# Happy <:> Blue <:> 10000
# Once upon a time
