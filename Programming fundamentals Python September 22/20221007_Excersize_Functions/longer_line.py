from math import sqrt
from math import floor


def points_distance(lst):  # calculates the distance between the lines
    x1, y1, x2, y2 = lst
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


def closer_to_center(lst):  # checks which pair is closest to zero
    x1, y1, x2, y2 = lst
    distance_1 = sqrt(pow(x1, 2) + pow(y1, 2))
    distance_2 = sqrt(pow(y2, 2) + pow(x2, 2))
    if distance_1 < distance_2:
        return "first_pair"
    return "second_pair"


first_line = [int(input()) for x in range(4)]  # filling the first coordinates
second_line = [int(input()) for y in range(4)]  # filling the second coordinates

first_length = 0    # variable for the distance from the first_line pairs
second_length = 0   # variable for the distance from the second_line pairs

# if the first pair is closer to the center just calculating the distance
if closer_to_center(first_line) == "first_pair":
    first_length = points_distance(first_line)

else:  # if the second pair is closer to the center: switch the places of the pairs in the list
    first_line = first_line[2:] + first_line[:2]
    first_length = points_distance(first_line)

# if the first pair is closer to the center just calculating the distance
if closer_to_center(second_line) == "first_pair":
    second_length = points_distance(second_line)
else:  # if the second pair is closer to the center: switch the places of the pairs in the list
    second_line = second_line[2:] + second_line[:2]
    second_length = points_distance(second_line)

# when we have the longer line: make the output with two tuples
if first_length >= second_length:
    first_tuple = (floor(first_line[0]), floor(first_line[1]))
    second_tuple = (floor(first_line[2]), floor(first_line[3]))
else:
    first_tuple = (floor(second_line[0]), floor(second_line[1]))
    second_tuple = (floor(second_line[2]), floor(second_line[3]))

print(f"{first_tuple}{second_tuple}")

# 40/100
# test inputs:

# 2
# 4
# -1
# 2
# -5
# -5
# 4
# -3

# 1
# 2
# 3
# 4
# 9
# 7
# 5
# 6
