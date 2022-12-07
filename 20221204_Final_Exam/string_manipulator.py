initial_string = input()

while True:

    command = input()
    if command == "End":
        break

    command = command.split()
    action = command[0]

    if action == "Translate":
        char = command[1]
        replacement = command[2]
        initial_string = initial_string.replace(char, replacement)
        print(initial_string)

    elif action == "Includes":
        substring = command[1]
        if substring in initial_string:
            print("True")
            continue
        print("False")

    elif action == "Start":
        substring = command[1]
        if initial_string.startswith(substring):
            print("True")
            continue
        print("False")

    elif action == "Lowercase":
        initial_string = initial_string.lower()
        print(initial_string)

    elif action == "FindIndex":
        char = command[1]
        for index in range(len(initial_string)-1, -1, -1):
            if initial_string[index] == char:
                print(index)
                break

    elif action == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        initial_string = initial_string[:start_index] + initial_string[start_index+count:]
        print(initial_string)

# test inputs:

# //Thi5 I5 MY 5trING!//
# Translate 5 s
# Includes string
# Start //This
# Lowercase
# FindIndex i
# Remove 0 10
# End

# *S0ftUni is the B3St Plac3**
# Translate 2 o
# Includes best
# Start the
# Lowercase
# FindIndex p
# Remove 2 7
# End
