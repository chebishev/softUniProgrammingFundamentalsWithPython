students = {}

while True:

    command = input().split(":")
    if len(command) == 1:
        key = command[0]
        key = key.replace("_", " ")
        for index in range(0, len(students[key]), 2):
            print(f"{students[key][index]} - {students[key][index + 1]}")
        break
    key = command[2]
    student = command[0]
    student_id = int(command[1])
    if key not in students:
        students[key] = []
    students[key].append(student)
    students[key].append(student_id)

# test inputs:

# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals

# Alex:6:programming basics
# Maria:7:programming basics
# Kaloyan:9:advanced
# Todor:10:fundamentals
# programming_basics
