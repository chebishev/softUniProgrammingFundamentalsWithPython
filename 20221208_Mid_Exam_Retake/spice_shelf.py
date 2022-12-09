spices_list = input().split(", ")

command = input()

while command != "done":

    command = command.split()
    action = command[0]

    if action == "AddSpice":
        spice = command[1]
        if spice not in spices_list:
            spices_list.append(spice)

    elif action == "AddManySpices":
        index = int(command[1])
        new_spices = command[2].split("|")
        new_spices_len = len(new_spices)
        for _ in range(new_spices_len):
            spices_list.insert(index, new_spices.pop())

    elif action == "SwapSpices":
        first_spice = command[1]
        second_spice = command[2]
        if first_spice in spices_list and second_spice in spices_list:
            first_index = spices_list.index(first_spice)
            second_index = spices_list.index(second_spice)
            spices_list[first_index], spices_list[second_index] = spices_list[second_index], spices_list[first_index]

    elif action == "ThrowAwaySpices":
        spice = command[1]
        number_of_spices_to_remove = int(command[2])
        spice_index = spices_list.index(spice)
        for _ in range(number_of_spices_to_remove):
            spices_list.pop(spice_index)

    elif action == "Arrange":
        spices_list.sort()

    command = input()

print(*spices_list, end=" ")
