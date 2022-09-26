from math import pi

type_of_figure = input()

result = 0

if type_of_figure == 'square':
    side = float(input())
    result = side * side
elif type_of_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    result = side_a * side_b
elif type_of_figure == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
else:
    side_a = float(input())
    side_b = float(input())
    result = (side_a * side_b) / 2

print(f'{result:.3f}')

# test input square 5
# test input rectangle 7 2.5
# test input circle 6
# test input triangle 4.5 20
