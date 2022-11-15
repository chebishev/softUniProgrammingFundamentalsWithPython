from math import sqrt
from math import floor


def center_point(x1, y1, x2, y2):
    distance_1 = sqrt(pow(x1, 2) + pow(y1, 2))
    distance_2 = sqrt(pow(y2, 2) + pow(x2, 2))
    if distance_1 <= distance_2:
        output_tuple = (x1, y1)
    else:
        output_tuple = (x2, y2)
    return output_tuple


x_one = floor(float(input()))
y_one = floor(float(input()))
x_two = floor(float(input()))
y_two = floor(float(input()))
print(center_point(x_one, y_one, x_two, y_two))

# test inputs:

# 2
# 4
# -1
# 2

# 10
# 14.5
# -17.2
# 16

