house_height = float(input())
wall_length = float(input())
wall_height = float(input())

side_walls_area = ((house_height * wall_length) * 2) - ((1.5 * 1.5) * 2)
front_back_walls_area = ((house_height * house_height) * 2) - (1.2 * 2)
house_area = side_walls_area + front_back_walls_area
paint_green = house_area / 3.4
roof_rectangles_area = 2 * (house_height * wall_length)
roof_triangles_area = 2 * (house_height * wall_height/2)
roof_area = roof_rectangles_area + roof_triangles_area
paint_red = roof_area / 4.3
print(f"{paint_green:.2f}")
print(f'{paint_red:.2f}')

# test input 6 10 5.2
# test input 10.25 15.45 8.88
