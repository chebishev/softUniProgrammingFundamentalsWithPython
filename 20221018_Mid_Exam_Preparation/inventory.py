def exists(lst, value):
    if value in lst:
        return True


collecting_items = input().split(", ")

while True:
    command = input().split(" - ")
    action = command[0]
    if action == "Craft!":
        break
    item = command[1]
    if action == "Collect":
        if not exists(collecting_items, item):
            collecting_items.append(item)
    elif action == "Drop":
        if exists(collecting_items, item):
            collecting_items.remove(item)
    elif action == "Combine Items":
        items = item.split(":")
        old_item = items[0]
        new_item = items[1]
        if exists(collecting_items, old_item):
            index = collecting_items.index(old_item)
            collecting_items.insert(index + 1, new_item)
    elif action == "Renew":
        if exists(collecting_items, item):
            collecting_items.append(collecting_items.pop(collecting_items.index(item)))

print(*collecting_items, sep=", ")

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
