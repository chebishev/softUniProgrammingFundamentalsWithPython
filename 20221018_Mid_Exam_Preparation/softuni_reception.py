first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
all_per_hour = first_employee_per_hour + second_employee_per_hour + third_employee_per_hour
students_count = int(input())
hours = 0

while True:
    if students_count <= 0:
        break
    hours += 1
    if hours % 4 == 0:
        continue
    students_count -= all_per_hour


print(f"Time needed: {hours}h.")

# test inputs:

# 5
# 6
# 4
# 20

# 1
# 2
# 3
# 45

# 3
# 2
# 5
# 40
