from math import ceil
wall_height = int(input())
wall_width = int(input())
percent_not_painted = int(input()) / 100
command = input()
painted_area = wall_height * wall_width * 4
painted_area -= painted_area * percent_not_painted

while command != "Tired!":
    litters = int(command)
    painted_area -= litters
    if painted_area == 0:
        print("All walls are painted! Great job, Pesho!")
        break
    if painted_area < 0:
        print(f"All walls are painted and you have {abs(ceil(painted_area))} l paint left!")
        break
    command = input()
    if command == "Tired!":
        print(f"{ceil(painted_area)} quadratic m left.")
        break

# test input 3 5 10 2 3 4 Tired!
# test input 2 3 25 6 7 8
