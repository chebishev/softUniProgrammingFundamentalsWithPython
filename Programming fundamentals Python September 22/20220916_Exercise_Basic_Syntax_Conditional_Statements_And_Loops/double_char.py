command = input()

while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    for index in range(len(command)):
        print(command[index]+command[index], end="")
    command = input()
    print()
    if command == "End":
        break

# test inputs:

# Hello World
# Repeat
# End

# 1234!
# SoftUni
# softuni
# End
