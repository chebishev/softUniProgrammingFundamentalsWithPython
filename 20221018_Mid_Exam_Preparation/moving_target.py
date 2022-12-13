def is_valid(lst, idx):
    if 0 <= idx < len(lst):
        return True
    return False


sequence_of_targets = [int(x) for x in input().split()]

while True:

    command = input()
    if command == "End":
        sequence_of_targets = [str(x) for x in sequence_of_targets]
        print("|".join(sequence_of_targets))
        break

    command = command.split()
    action = command[0]
    index = int(command[1])

    if action == "Shoot":
        power = int(command[2])
        if is_valid(sequence_of_targets, index):
            sequence_of_targets[index] -= power
            if sequence_of_targets[index] <= 0:
                sequence_of_targets.pop(index)

    elif action == "Add":
        value = int(command[2])
        if is_valid(sequence_of_targets, index):
            sequence_of_targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(command[2])
        if is_valid(sequence_of_targets, index) and \
                is_valid(sequence_of_targets, index - radius) and \
                is_valid(sequence_of_targets, index + radius):
            sequence_of_targets = sequence_of_targets[:index-radius] + sequence_of_targets[index+radius + 1:]

        else:
            print("Strike missed!")

# test inputs:

# 52 74 23 44 96 110
# Shoot 5 10
# Shoot 1 80
# Strike 2 1
# Add 22 3
# End

# 1 2 3 4 5
# Strike 0 1
# End
