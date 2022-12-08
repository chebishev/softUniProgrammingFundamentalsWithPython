def index_is_valid(index, list):
    if 0 <= index < len(list):
        return True
    return False


game_elements = input().split()
counter = 0

while True:

    command = input()
    if command == "end":
        if game_elements:
            print(f"Sorry you lose :(\n{' '.join(game_elements)}")
        break

    command = command.split()
    first_index = int(command[0])
    second_index = int(command[1])
    if first_index == second_index or \
            not index_is_valid(first_index, game_elements) or \
            not index_is_valid(second_index, game_elements):
        counter += 1
        new_element = "-" + str(counter) + 'a'
        new_index = len(game_elements) // 2
        game_elements.insert(new_index, new_element)
        game_elements.insert(new_index, new_element)
        print("Invalid input! Adding additional elements to the board")

        continue

    if game_elements[first_index] == game_elements[second_index]:
        print(f"Congrats! You have found matching elements - {game_elements[first_index]}!")
        counter += 1
        if second_index > first_index:
            game_elements.pop(second_index)
            game_elements.pop(first_index)
        elif first_index > second_index:
            game_elements.pop(first_index)
            game_elements.pop(second_index)
    else:
        counter += 1
        print("Try again!")

    if not game_elements:
        print(f"You have won in {counter} turns!")
        break

# test inputs:

# 1 1 2 2 3 3 4 4 5 5
# 1 0
# -1 0
# 1 0
# 1 0
# 1 0
# end

# a 2 4 a 2 4
# 0 3
# 0 2
# 0 1
# 0 1
# end

