targets = [int(x) for x in input().split()]
counter = 0
while True:

    command = input()
    if command == "End":
        break

    index_to_shoot = int(command)
    if 0 <= index_to_shoot < len(targets):
        current_number = targets[index_to_shoot]
        targets[index_to_shoot] = -1
        counter += 1
        for index in range(len(targets)):
            if targets[index] == -1:
                continue
            elif targets[index] > current_number:
                targets[index] -= current_number
            else:
                targets[index] += current_number

print(f"Shot targets: {counter} ->", *targets, end=" ")

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
