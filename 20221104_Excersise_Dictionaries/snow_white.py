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


for color in sorted(dwarf_dictionary, key=lambda x: len(dwarf_dictionary[x]), reverse=True):
    for dwarf, physics in sorted(dwarf_dictionary.items(), reverse=True):
        key, value = dwarf_dictionary[color].items()
        print(f"({dwarf}) {key} <-> {value}")

