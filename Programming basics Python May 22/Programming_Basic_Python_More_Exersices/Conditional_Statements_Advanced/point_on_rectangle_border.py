position_x_one = int(input())
position_y_one = int(input())
position_x_two = int(input())
position_y_two = int(input())
position_x = float(input())
position_y = float(input())
position = ""

if (position_x == position_x_one or position_x == position_x_two) and position_y_one < position_y < position_y_two:
    position = "Border"
elif (position_y == position_y_one or position_y == position_y_two) and position_x_one < position_x < position_x_two:
    position = "Border"
elif position_x == position_x_one and position_y == position_y_two:
    position = "Border"
else:
    position = "Inside / Outside"

print(position)

# test input 2 -3 12 3 8 -1
# test input 2 - 12 3 12 -1
