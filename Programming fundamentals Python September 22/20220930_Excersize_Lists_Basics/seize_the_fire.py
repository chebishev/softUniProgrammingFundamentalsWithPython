fire_information = input().split("#")
water_amount = int(input())
effort = 0
total_fire = 0
is_valid = False
print("Cells:")
while water_amount >= 0:
    if len(fire_information) == 0:
        break
    current_item = fire_information.pop(0).split(" = ")
    fire_level = current_item[0]
    cell = int(current_item[1])
    if fire_level == "High" and 81 <= cell <= 125:
        is_valid = True
    elif fire_level == "Medium" and 51 <= cell <= 80:
        is_valid = True
    elif fire_level == "Low" and 1 <= cell <= 50:
        is_valid = True
    else:
        is_valid = False
    if is_valid and water_amount >= cell:
        water_amount -= cell
        effort += 0.25 * cell
        total_fire += cell
        print(f" - {cell}")
    is_valid = False
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

# test inputs:

# High = 89#Low = 28#Medium = 77#Low = 23
# 1250

# High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77
# 220
