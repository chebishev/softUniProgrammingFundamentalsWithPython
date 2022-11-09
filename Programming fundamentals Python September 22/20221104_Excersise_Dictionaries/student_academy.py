students_count = int(input())
students_dictionary = {}

for index in range(students_count):
    name = input()
    grade = float(input())

    if name not in students_dictionary.keys():
        students_dictionary[name] = []
    students_dictionary[name].append(grade)

for key, value in students_dictionary.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.50:
        print(f"{key} -> {average_grade:.2f}")

# test inputs:

# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5

# 5
# Amanda
# 3.5
# Amanda
# 4
# Rob
# 5.5
# Christian
# 5
# Robert
# 6

