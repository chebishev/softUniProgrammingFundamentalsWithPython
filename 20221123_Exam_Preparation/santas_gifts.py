def is_valid(lst, idx):
    if 0 <= idx < len(lst):
        return True
    return False


number_of_commands = int(input())
houses = list(map(int, input().split()))
last_position = 0
for _ in range(number_of_commands):
    command = input().split()

    if len(command) == 2:
        action = command[0]
        steps = int(command[1])
        current_position = 0
        if action == "Forward":
            current_position = last_position + steps
            if is_valid(houses, current_position):
                houses.pop(current_position)
                last_position = current_position
            else:
                continue
        elif action == "Back":
            current_position = last_position - steps
            if is_valid(houses, current_position):
                houses.pop(current_position)
                last_position = current_position
            else:
                continue

    elif len(command) == 3:
        action, first_value, second_value = command[0], int(command[1]), int(command[2])
        if action == "Gift":
            index = first_value
            new_element = second_value
            if is_valid(houses, index):
                houses.insert(index, new_element)
                last_position = index
        elif action == "Swap":
            if first_value in houses and second_value in houses:
                first_index = houses.index(first_value)
                second_index = houses.index(second_value)
                houses[first_index], houses[second_index] = houses[second_index], houses[first_index]

print(f"Position: {last_position}")
houses = [str(x) for x in houses]
print(", ".join(houses))

# test inputs:

# 5
# 255 500 54 78 98 24 30 47 69 58
# Forward 1
# Swap 54 47
# Gift 1 20
# Back 1
# Forward 3

# 6
# 50 40 25 63 78 54 66 77 24 87
# Forward 4
# Back 3
# Forward 3
# Gift 2 88
# Swap 50 87
# Forward 1
