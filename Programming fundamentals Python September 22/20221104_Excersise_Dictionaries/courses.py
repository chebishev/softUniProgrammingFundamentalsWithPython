courses_dictionary = {}

while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses_dictionary.keys():
        courses_dictionary[course_name] = []
    courses_dictionary[course_name].append(student_name)

for key in courses_dictionary.keys():
    print(f"{key}: {len(courses_dictionary[key])}")
    for student in courses_dictionary[key]:
        print(f"-- {student}")

# test inputs:

# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end

# Algorithms : Jay Moore
# Programming Basics : Martin Taylor
# Python Fundamentals : John Anderson
# Python Fundamentals : Andrew Robinson
# Algorithms : Bob Jackson
# Python Fundamentals : Clark Lewis
# end
