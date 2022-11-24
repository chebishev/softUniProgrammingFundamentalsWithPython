to_do_list = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    current_command = command.split("-")
    priority = int(current_command[0]) - 1
    task = current_command[1]
    to_do_list.pop(priority)
    to_do_list.insert(priority, task)
result = [element for element in to_do_list if element != 0]
print(result)

# test inputs:

# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End

# 3-C
# 2-A
# 1-B
# 6-V
# End
