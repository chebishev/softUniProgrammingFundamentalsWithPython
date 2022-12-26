def valid_position(direction):
    if direction in maze:
        return True
    return False

def not_wall(direction):
    if direction == " ":
        return True
    return False

def exit(matrix, row, col):
    if matrix[row] == 0 or matrix[row] == len(matrix) - 1 and col == 0 or col == len(matrix[row]) -1:
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
    if is_found:
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
    left = maze[initial_row][initial_index - 1]
    right = maze[initial_row][initial_index + 1]
    up = maze[initial_row - 1][initial_index]
    down = maze[initial_row + 1][initial_index]
    if valid_position(left) \
        and not_wall(maze, initial_row, initial_index - 1):
        maze[initial_row][initial_index - 1] = "k"
        initial_index -= 1
        
    elif valid_position(maze, initial_row, initial_index + 1):
        initial_index = initial_index + 1
    elif valid_position(maze, initial_row-1, initial_index):
        initial_row = initial_row - 1
    elif valid_position(maze, initial_row + 1, initial_index):
        initial_row = initial_row + 1
    else:
        break
    if exit(maze, initial_row, initial_index):
            exit_found = True
            break

if exit_found:
    print()
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
