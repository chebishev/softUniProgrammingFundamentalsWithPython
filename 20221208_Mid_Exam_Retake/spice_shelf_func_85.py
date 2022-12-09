def add_spice(lst, ingredient):
    if ingredient not in lst:
        lst.append(ingredient)
    return lst


def add_many_spices(lst, idx, new_list):
    spices_to_add = len(new_list)
    for _ in range(spices_to_add):
        current_spice = new_list.pop()
        lst.insert(idx, current_spice)
    return lst


def swap_spices(lst, first, second):
    if first in lst and second in lst:
        first_index = lst.index(first)
        second_index = lst.index(second)
        lst[first_index], lst[second_index] = lst[second_index], lst[first_index]
        return lst


def throw_spices(lst, ingredient, number):
    if ingredient in lst:
        ingredient_index = lst.index(ingredient)
        for _ in range(number):
            lst.pop(ingredient_index)
        return lst


spice_shelf = input().split(", ")

while True:

    command = input()
    if command == "done":
        break

    command = command.split()
    action = command[0]

    if action == "AddSpice":
        spice = command[1]
        spice_shelf = add_spice(spice_shelf, spice)

    elif action == "AddManySpices":
        index = int(command[1])
        spices = command[2].split("|")
        spice_shelf = add_many_spices(spice_shelf, index, spices)

    elif action == "SwapSpices":
        first_spice = command[1]
        second_spice = command[2]
        spice_shelf = swap_spices(spice_shelf, first_spice, second_spice)

    elif action == "ThrowAwaySpices":
        spice = command[1]
        spices_to_remove = int(command[2])
        spice_shelf = throw_spices(spice_shelf, spice, spices_to_remove)

    elif action == "Arrange":
        spice_shelf.sort()

print(f"{' '.join(spice_shelf)}")


# test inputs:

# coriander, cloves, paprika, allspice, turmeric, anise, cumin
# AddSpice nutmeg
# ThrowAwaySpices cloves 3
# AddManySpices 3 cayenne|cardamom|mace
# done

# coriander, cloves, paprika, cumin
# AddSpice nutmeg
# AddSpice anise
# AddSpice turmeric
# AddSpice cumin
# SwapSpices coriander paprika
# ThrowAwaySpices cumin 4
# done
