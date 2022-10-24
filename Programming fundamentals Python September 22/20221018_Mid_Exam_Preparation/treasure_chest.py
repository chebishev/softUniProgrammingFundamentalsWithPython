def main_func(data):
    while True:
        command = input()
        new_list = []

        sum_items = 0
        count = 0
        if command == "Yohoho!":
            break
        current_command = command.split()
        if current_command[0] == "Loot":
            current_command.pop(0)
            for char in current_command:
                if char not in data:
                    data.insert(0, char)
        if current_command[0] == "Drop":
            if 0 <= int(current_command[1]) < len(data):
                removed = data.pop(int(current_command[1]))
                data.append(removed)

        if current_command[0] == "Steal":
            new_list = data[- int(current_command[1]):]
            print(new_list)
    avg = 0
    for letter in data:
        avg += len(letter)
    avg /= len(data)
    empty_chest = []
    if new_list == empty_chest:
        print("Failed treasure hunt.")
    else:
        print(f"Average treasure gain: {avg:.2f} pirate credits.")


initial_treasure_chest = input().split("|")
main_func(initial_treasure_chest)