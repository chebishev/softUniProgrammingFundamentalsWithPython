def collect(list, item):
    if item not in list:
        list.append(item)
    return list

def drop(list, item):
    if item in list:
        list.remove(item)
    return list

def combine_items(list, old, new):
    if old in list:
        index = list.index(old) + 1
        list.insert(index, new)
    return list

def renew(list, item):
    if item in list:
        item_index = list.index(item)
        list.append(list.pop(item_index))
    return list    

initial_items = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        print(", ".join(initial_items))
        break
    command = command.split(" - ")
    action = command[0]
    material = command[1]

    if action == "Collect":
        initial_items = collect(initial_items, material)

    elif action == "Drop":
        initial_items = drop(initial_items, material)

    elif action == "Combine Items":
        old_item, new_item = material.split(":")
        initial_items = combine_items(initial_items, old_item, new_item)

    elif action == "Renew":
        initial_items = renew(initial_items, material)

# test inputs:

# Iron, Wood, Sword
# Collect - Gold
# Drop - Wood
# Craft!

# Iron, Sword
# Drop - Bronze
# Combine Items - Sword:Bow
# Renew - Iron
# Craft!
