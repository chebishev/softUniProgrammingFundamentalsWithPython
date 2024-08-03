labyrinth_size = int(input())
labyrinth = []  # matrix with "#" as walls, "k" as Kate position and " " as possible cells for the player to move
path_list = []  # it contains the path of the player in format [U, R, D, L]
exit_found = False  # flag for the output print
max_path_length = 0  # stores the max length of the path if the player reaches the exit
kate_position = ()  # stores the initial position of the player

for index in range(labyrinth_size):
    row = list(input())
    if "k" in row:
        kate_position = (index, row.index("k"))
    labyrinth.append(row)


def find_paths(row, col, direction, labyrinth, path_list):
    if row < 0 or col < 0 or row >= len(labyrinth) or col >= len(labyrinth[0]):
        global exit_found
        exit_found = True
        global max_path_length
        if max_path_length < len(path_list):
            max_path_length = len(path_list)
        return
    if labyrinth[row][col] == "v":
        return
    if labyrinth[row][col] == "#":
        return

    path_list.append(direction)

    labyrinth[row][col] = "v"  # mark the cell as visited
    # recursive calls for the 4 directions
    find_paths(row - 1, col, "U", labyrinth, path_list)
    find_paths(row, col + 1, "R", labyrinth, path_list)
    find_paths(row + 1, col, "D", labyrinth, path_list)
    find_paths(row, col - 1, "L", labyrinth, path_list)
    labyrinth[row][col] = " "  # mark the cell as unvisited


find_paths(kate_position[0], kate_position[1], "", labyrinth, path_list)

if exit_found:
    print(f"Kate got out in {max_path_length} moves")
else:
    print("Kate cannot get out")

# test inputs:

# 4
# ######
# ##  k#
# ## ###
# ## ###

# 5
# ######
# ##  k#
# ## ###
# ######
# ## ###
