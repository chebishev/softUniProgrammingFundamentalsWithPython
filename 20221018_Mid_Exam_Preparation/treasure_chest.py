def loot_func(treasure_chest, current_command):
    current_command.pop(0)

    for element in current_command:
        if element not in treasure_chest:
            treasure_chest.insert(0, element)

    return treasure_chest


def drop_func(treasure_chest, index):
    if 0 <= index < len(treasure_chest):
        treasure_chest.append(treasure_chest.pop(index))

    return treasure_chest


def steal_func(treasure_chest, count):
    stealed = []
    for i in range(int(count)):
        stealed.append(treasure_chest.pop())
    stealed = stealed[::-1]
    print(', '.join(stealed))

    return treasure_chest


initial_treasure_chest = input().split('|')

while True:

    command = input()
    if command == 'Yohoho!':
        break
    current_command = command.split(' ')

    if current_command[0] == 'Loot':
        initial_treasure_chest = loot_func(initial_treasure_chest, current_command)
    elif current_command[0] == 'Drop':
        initial_treasure_chest = drop_func(initial_treasure_chest, int(current_command[1]))
    elif current_command[0] == 'Steal':
        initial_treasure_chest = steal_func(initial_treasure_chest, int(current_command[1]))

if len(initial_treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    total_gain = 0
    for i in range(len(initial_treasure_chest)):
        total_gain += len(initial_treasure_chest[i])
    average_gain = total_gain / len(initial_treasure_chest)
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')