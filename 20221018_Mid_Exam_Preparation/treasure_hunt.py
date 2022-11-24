treasure_chest = input().split("|")
stolen_items = []
hunt_is_failed = False
while True:
    command = input().split()
    if command[0] == "Yohoho!":
        break
    action = command[0]
    if action == "Loot":
        for loot in range(1, len(command)):
            if command[loot] not in treasure_chest:
                treasure_chest.insert(0, command[loot])
    elif action == "Drop":
        index = int(command[1])
        if -len(treasure_chest) <= index < len(treasure_chest):
            dropped_item = treasure_chest.pop(index)
            treasure_chest.append(dropped_item)
        else:
            continue
    elif action == "Steal":
        items_count = -int(command[1])
        for index in range(items_count, 0):
            if len(treasure_chest) > 0:
                if index < -len(treasure_chest):
                    stolen_items = treasure_chest
                    hunt_is_failed = True
                    break
                else:
                    stolen_items.append(treasure_chest.pop(index))
                    if len(treasure_chest) <= 0:
                        hunt_is_failed = True
                        break
            else:
                hunt_is_failed = True
                break
        print(*stolen_items, sep=", ")
        stolen_items.clear()
if hunt_is_failed:
    print("Failed treasure hunt.")
else:
    average = 0
    for item in treasure_chest:
        average += len(item)
    average /= len(treasure_chest)
    print(f"Average treasure gain: {average:.2f} pirate credits.")

# test inputs:

# Gold|Silver|Bronze|Medallion|Cup
# Loot Wood Gold Coins
# Loot Silver Pistol
# Drop 3
# Steal 3
# Yohoho!

# Diamonds|Silver|Shotgun|Gold
# Loot Silver Medals Coal
# Drop -1
# Drop 1
# Steal 6
# Yohoho!
