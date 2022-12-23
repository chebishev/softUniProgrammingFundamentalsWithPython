rows = int(input())
battle_ships_list = []
ships_destroyed = 0

for row in range(rows):
    current_row = [int(x) for x in input().split()]
    battle_ships_list.append(current_row)

targets_list = input().split()
for square in targets_list:
    current_square = square.split("-")
    row, col = int(current_square[0]), int(current_square[1])
    if battle_ships_list[row][col] > 0:
        battle_ships_list[row][col] -= 1
        if battle_ships_list[row][col] == 0:
            ships_destroyed += 1
    else:
        continue
print(ships_destroyed)

# test inputs:

# 3
# 1 0 0 1
# 2 0 0 0
# 0 3 0 1
# 0-0 1-0 2-1 2-1 2-1 1-1 2-1

# 5
# 1 0 5 0 1
# 6 3 9 0 0
# 7 9 4 3 2
# 1 0 0 4 9
# 5 6 0 3 5
# 0-1 0-2 0-2 0-2 0-2 0-2 3-0
