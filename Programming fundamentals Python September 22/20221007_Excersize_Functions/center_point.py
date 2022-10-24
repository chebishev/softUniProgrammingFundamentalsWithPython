def center_point(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        output_tuple = (int(x1), int(y1))
    else:
        output_tuple = (int(x2), int(y2))
    return output_tuple


x_one = float(input())
y_one = float(input())
x_two = float(input())
y_two = float(input())
print(center_point(x_one, y_one, x_two, y_two))

# not finished
