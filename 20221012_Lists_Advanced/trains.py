wagons = int(input())
train = [0] * wagons

while True:
    command = input()

    if command == "End":
        break
    current_command = command.split(" ")
    action = current_command[0]

    if action == "add":
        train[-1] += int(current_command[1])
    elif action == "insert" or action == "leave":
        index = int(current_command[1])
        people = int(current_command[2])
        if action == "insert":
            train[index] += people
        else:
            train[index] -= people

print(train)

# test inputs:

# 3
# add 20
# insert 0 15
# leave 0 5
# End	[10, 0, 20]

# 5
# add 10
# add 20
# insert 0 16
# insert 1 44
# leave 1 12
# insert 2 100
# insert 4 61
# leave 4 1
# add 15
# End
