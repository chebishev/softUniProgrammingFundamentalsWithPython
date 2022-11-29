pokemon_list = list(map(int, input().split()))
total = 0
while pokemon_list:
    index = int(input())
    removed_pokemon = 0
    if index < 0:
        removed_pokemon = pokemon_list.pop(0)
        pokemon_list.insert(0, pokemon_list[-1])

    elif index >= len(pokemon_list):
        removed_pokemon = pokemon_list.pop()
        pokemon_list.insert(index, pokemon_list[0])
    else:
        removed_pokemon = pokemon_list.pop(index)

    for number in range(len(pokemon_list)):
        if pokemon_list[number] <= removed_pokemon:
            pokemon_list[number] += removed_pokemon
        elif pokemon_list[number] > removed_pokemon:
            pokemon_list[number] -= removed_pokemon

    total += removed_pokemon

print(total)

# test inputs:

# 4 5 3
# 1
# 1
# 0

# 5 10 6 3 5
# 2
# 4
# 1
# 1
# 3
# 0
# 0
