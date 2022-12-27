def valid_position(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        return True
    return False


def not_wall(direction):
    if direction == " ":
        return True
    return False


def exit(matrix, row, col):
    if row == 0 and 0 <= col < len(matrix[row]) \
            or row == len(matrix) - 1 and 0 <= col < len(matrix[row]) \
            or col == 0 and 0 <= row < len(matrix[row][col]) \
            or col == len(matrix[row]) - 1 and 0 <= row < len(matrix[row][col]):
        return True
    return False


maze_rows = int(input())
#   # - wall
#  " " - empty space
#   k - initial position of Kate
maze = []
for row in range(maze_rows):
    current_row = [x for x in input()]
    maze.append(current_row)
start_row = 0
start_index = 0
initial_index = 0
initial_row = 0
path_counter = 0
k_is_found = False
exit_found = False
for index in range(len(maze)):
    if k_is_found:
        break
    row = maze[index]
    if "k" in row:
        for position in row:
            if position == "k":
                initial_index = row.index(position)
                start_index = row.index(position)
                initial_row = index
                start_row = index
                k_is_found = True
                break

while True:
    wall_counter = 0
    if valid_position(maze, initial_row, initial_index - 1):
        left = maze[initial_row][initial_index - 1]
        if not_wall(left):
            if exit(maze, initial_row, initial_index - 1):
                exit_found = True
                break
            else:
                maze[initial_row][initial_index - 1] = "k"
                initial_index -= 1
        else:
            wall_counter += 1
    if valid_position(maze, initial_row, initial_index + 1):
        right = maze[initial_row][initial_index + 1]
        if not_wall(right):
            if exit(maze, initial_row, initial_index + 1):
                exit_found = True
                break
            else:
                maze[initial_row][initial_index + 1] = "k"
                initial_index += 1
        else:
            wall_counter += 1
    if valid_position(maze, initial_row - 1, initial_index):
        up = maze[initial_row - 1][initial_index]
        if not_wall(up):
            if exit(maze, initial_row - 1, initial_index):
                exit_found = True
                break
            else:
                maze[initial_row - 1][initial_index] = "k"
                initial_row = initial_row - 1
        else:
            wall_counter += 1
    if valid_position(maze, initial_row + 1, initial_index):
        down = maze[initial_row + 1][initial_index]
        if not_wall(down):
            if exit(maze, initial_row + 1, initial_index):
                exit_found = True
                break
            else:
                maze[initial_row + 1][initial_index] = "k"
                initial_row = initial_row + 1
        else:
            wall_counter += 1
    if wall_counter == 4:
        break

if exit_found:
    print("Yes")
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
