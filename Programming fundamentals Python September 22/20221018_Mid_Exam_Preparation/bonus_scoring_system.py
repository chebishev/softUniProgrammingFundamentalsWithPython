from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
current_attendances = 0

for attendance in range(number_of_students):
    student_attendances = int(input())
    total_bonus = (student_attendances / number_of_lectures) * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        current_attendances = student_attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {current_attendances} lectures.")

# test inputs:

# 5
# 25
# 30
# 12
# 19
# 24
# 16
# 20

# 10
# 30
# 14
# 8
# 23
# 27
# 28
# 15
# 17
# 25
# 26
# 5
# 18
