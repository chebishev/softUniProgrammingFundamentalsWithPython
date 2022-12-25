def valid_position(matrix, row, col):
    if 0 <= row < len(maze) and 0 <= col < len(maze[row]):
        return True
    return False

def not_wall(maze, row, col):
    if maze[row][cow] == " ":
        return True
    return False

def exit():
    if maze[row] == 0 or maze[row] == len(maze) - 1 and col == 0 or col == len(maze[row]) -1:
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
is_found = False
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
                is_found = True
                break

while True:
    if valid_position(maze, initial_row, initial_index -1) \
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
