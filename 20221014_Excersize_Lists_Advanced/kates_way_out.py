maze_rows = int(input())
#   # - wall
#  " " - empty space
#   k - initial position of Kate
maze = []
for row in range(maze_rows):
    current_row = [x for x in input()]
    maze.append(current_row)

initial_index = 0
initial_row = 0
for index in range(len(maze)):
    row = maze[index]
    if "k" in row:
        for position in row:
            if position == "k":
                initial_index = row.index(position)
                initial_row = index
                break

print(initial_row)
print(initial_index)

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
