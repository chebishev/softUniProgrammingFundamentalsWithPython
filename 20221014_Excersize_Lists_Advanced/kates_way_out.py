# This function checks if the row and the column are in the borders of the maze
def valid_position(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        return True


# This will check if the given coordinates are valid move (not "#" or "k")
def not_wall(matrix, row, col):
    if matrix[row][col] == " ":
        return True


# This function checks if the current move is on one of the borders of the maze, which means that the exit is found
def exit(matrix, row, col):
    if row == 0 and 0 <= col < len(matrix[row]) \
            or row == len(matrix) - 1 and 0 <= col < len(matrix[row]) \
            or col == 0 and 0 <= row < len(matrix[row][col]) \
            or col == len(matrix[row]) - 1 and 0 <= row < len(matrix[row][col]):
        return True


maze_rows = int(input())  # integer that gives us the number of the rows. We will use it as a range in the for loop
maze = []  # empty list, which will take all the rows with the given data from the following for loop
start_row = 0  # this will keep the start position of Kate as a Row number
start_index = 0  # this will keep the start position of Kate as a Column number
y = 0  # current row
x = 0  # current column
for row in range(maze_rows):
    current_row = [x for x in input()]  # converting the row data from string to list of elements
    maze.append(current_row)  # adding the current row to the list

    if "k" in current_row:
        start_row = row
        x = row
        k_index = maze[row].index("k")
        start_index = k_index
        y = k_index

exit_found = False  # with this we will break the while loop if the first exit is found
path_list = [(start_row, start_index)]  # we are using it as a counter (by length) at the final
while True:

    # check for valid left position and " " on the left direction
    if valid_position(maze, x, y - 1) and not_wall(maze, x, y - 1):
        if exit(maze, x, y - 1):
            exit_found = True
            break
        maze[x][y - 1] = "k"  # marks the current spot as visited and on future check it will be considered as a wall
        path_list.append("left")
        y -= 1  # update current column

    # check for valid right position and " " on the right direction
    elif valid_position(maze, x, y + 1) and not_wall(maze, x, y + 1):
        if exit(maze, x, y + 1):
            exit_found = True
            break
        maze[x][y + 1] = "k"
        path_list.append("right")
        y += 1  # update current column

    # check for valid up position and " " on the up direction
    elif valid_position(maze, x - 1, y) and not_wall(maze, x - 1, y):
        if exit(maze, x - 1, y):
            exit_found = True
            break
        maze[x - 1][y] = "k"
        path_list.append("up")
        x -= 1  # update current row

    # check for valid down position and " " on the down direction
    elif valid_position(maze, x + 1, y) and not_wall(maze, x + 1, y):
        if exit(maze, x + 1, y):
            exit_found = True
            break
        maze[x + 1][y] = "k"
        path_list.append("down")
        x += 1  # update current row
    else:
        break

if exit_found:
    print(f"Kate got out in {len(path_list) + 1} moves")
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
