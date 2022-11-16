from math import sqrt


def points_distance(lst):  # calculates the distance between the lines
    x1, y1, x2, y2 = lst
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


def closer_to_center(lst):  # checks which pair is closest to zero and returns it in right order
    x1, y1, x2, y2 = lst
    distance_1 = sqrt(pow(x1, 2) + pow(y1, 2))
    distance_2 = sqrt(pow(y2, 2) + pow(x2, 2))
    if distance_1 < distance_2:
        return lst
    lst = lst[2:] + lst[:2]
    return lst


def output(lst):   # formatting the output
    lst = closer_to_center(lst)
    return f"({int(lst[0])}, {int(lst[1])})({int(lst[2])}, {int(lst[3])})"


first_line = [int(input()) for x in range(4)]  # filling the first coordinates
second_line = [int(input()) for y in range(4)]  # filling the second coordinates

first_length = points_distance(first_line)
second_length = points_distance(second_line)

# when we have the longer line: make the output
if first_length >= second_length:
    print(output(first_line))
else:
    print(output(second_line))

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
