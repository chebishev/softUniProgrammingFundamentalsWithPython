board_rows = int(input())
dots_list = []
dots_counter = 0
dot_found = False
for row in range(board_rows):
    current_row = input().split()
    dots_list.append(current_row)

current_dots = 0
for row in range(len(dots_list)):
    for col in range(len(dots_list[row])):
        if dots_list[row][col] == ".":
            if dot_found:
                # just in case: all directions from current position. 
                # They need to be checked for valid indexing
                # So.. function will do the job
                current_position = dots_list[row][col]
                up = dots_list[row-1][col]
                down = dots_list[row+1][col]
                left = dots_list[row][col-1]
                right = dots_list[row][col+1]
                current_dots += 1

            else:
                dot_found = True
                current_dots = 0
        else:
            dot_found = False
            continue
print("\n".join(dots_list))

# test inputs:

# 5
# . . - - -
# . . - - -
# - - - - -
# - - - . .
# - - - . .

# 6
# . . - . - .
# - . . . . .
# - . - - - -
# - . . - - -
# - . . . . -
# - - - . . -

# 4
# - . - . . –
# . - . . - .
# . - - - - -
# - - - . - -
