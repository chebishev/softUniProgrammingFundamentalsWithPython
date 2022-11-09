number_of_lines = int(input())
tank_capacity = 0

for litters in range(number_of_lines):
    temp_litters = int(input())
    if temp_litters + tank_capacity > 255:
        print("Insufficient capacity!")
    else:
        tank_capacity += temp_litters

print(tank_capacity)

# test inputs:

# 