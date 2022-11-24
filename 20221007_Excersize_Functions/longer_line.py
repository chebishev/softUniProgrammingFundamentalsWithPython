# WORKING SOLUTION FROM SOFTUNI FORUMS:

# from math import floor
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x3 = float(input())
# y3 = float(input())
# x4 = float(input())
# y4 = float(input())
#
# def distance(_x1, _y1, _x2, _y2):
#     return (_x2-_x1)**2 + (_y2-_y1)**2
#
# x1y1 = distance(x1, y1, 0, 0)
# x2y2 = distance(x2, y2, 0, 0)
# x3y3 = distance(x3, y3, 0, 0)
# x4y4 = distance(x4, y4, 0, 0)
#
# line_1 = x1y1 + x2y2
# line_2 = x3y3 + x4y4
#
# if line_1 >= line_2:
#     if x1y1 <= x2y2:
#         print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
#     else:
#         print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')
# if line_1 < line_2:
#     if x3y3 <= x4y4:
#         print(f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})')
#     else:
#         print(f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})')

from math import floor


def points_distance(lst):  # calculates the distance between the lines
    x1, y1, x2, y2 = lst
    return (x2 - x1)**2 + (y2 - y1)**2


def closer_to_center(lst):  # checks which pair is closest to zero and returns it in right order
    x1, y1, x2, y2 = lst
    distance_1 = pow(x1, 2) + pow(y1, 2)
    distance_2 = pow(y2, 2) + pow(x2, 2)
    if distance_1 < distance_2:
        return f"({floor(lst[0])}, {floor(lst[1])})({floor(lst[2])}, {floor(lst[3])})"
    lst = lst[2:] + lst[:2]
    return f"({floor(lst[0])}, {floor(lst[1])})({floor(lst[2])}, {floor(lst[3])})"


first_line = [float(input()) for x in range(4)]  # filling the first coordinates
second_line = [float(input()) for y in range(4)]  # filling the second coordinates
first_length = points_distance(first_line)
second_length = points_distance(second_line)

# when we have the longer line: make the output
if first_length >= second_length:
    print(closer_to_center(first_line))
if second_length > first_length:
    print(closer_to_center(second_line))

# 60/100
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
