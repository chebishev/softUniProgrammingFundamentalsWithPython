initial_list = input().split("!")

while True:
    command = input().split()
    action = command[0]
    item = command[1]

    if action == "Go":
        break

    if action == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)

    elif action == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)

    elif action == "Correct":
        new_item = command[2]
        if item in initial_list:
            index = initial_list.index(item)
            initial_list.remove(item)
            initial_list.insert(index, new_item)

    elif action == "Rearrange":
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

print(*initial_list, sep=", ")

# test inputs:

# Tomatoes!Potatoes!Bread
# Unnecessary Milk
# Urgent Tomatoes
# Go Shopping!

# Milk!Pepper!Salt!Water!Banana
# Urgent Salt
# Unnecessary Grapes
# Correct Pepper Onion
# Rearrange Grapes
# Correct Tomatoes Potatoes
# Go Shopping!
