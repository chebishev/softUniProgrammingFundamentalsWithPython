targets_sequence = list(map(int, input().split()))

while True:
    command = input()

    if command == "End":
        break

    index = int(command)
    if 0 <= index < len(targets_sequence) and targets_sequence[index] != -1:
        current_shot = targets_sequence[index]
        targets_sequence[index] = -1
        for position in range(len(targets_sequence)):
            if targets_sequence[position] != -1:
                if targets_sequence[position] > current_shot:
                    targets_sequence[position] -= current_shot
                else:
                    targets_sequence[position] += current_shot

count = [hit for hit in targets_sequence if hit == -1]
print(f"Shot targets: {len(count)} ->", *targets_sequence, sep=" ")

# test inputs:

# 24 50 36 70
# 0
# 4
# 3
# 1
# End

# 30 30 12 60 54 66
# 5
# 2
# 4
# 0
# End
