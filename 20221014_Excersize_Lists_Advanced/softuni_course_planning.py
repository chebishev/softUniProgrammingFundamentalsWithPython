initial_schedule = input().split(", ")

while True:

    command = input()
    if command == "course start":
        break

    command = command.split(":")
    action = command[0]
    lesson_title = command[1]
    exercise = lesson_title + "-Exercise"

    if action == "Add":
        if lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)

    elif action == "Insert":
        index = int(command[2])
        if lesson_title not in initial_schedule:
            initial_schedule.insert(index, lesson_title)

    elif action == "Remove":
        if lesson_title in initial_schedule:
            initial_schedule.remove(lesson_title)
        if exercise in initial_schedule:
            initial_schedule.remove(exercise)

    elif action == "Swap":
        new_lesson = command[2]
        new_exercise = new_lesson + "-Exercise"
        if lesson_title in initial_schedule and new_lesson in initial_schedule:
            index, new_index = initial_schedule.index(lesson_title), initial_schedule.index(new_lesson)
            initial_schedule[index], initial_schedule[new_index] = new_lesson, lesson_title
            if exercise in initial_schedule and new_exercise in initial_schedule:
                initial_schedule[index + 1], initial_schedule[new_index + 1] = new_exercise, exercise
            elif exercise in initial_schedule:
                for position in range(len(initial_schedule)):
                    if initial_schedule[position] == exercise:
                        initial_schedule[position] = "0"
                initial_schedule.insert(new_index + 1, exercise)
            elif new_exercise in initial_schedule:
                for position in range(len(initial_schedule)):
                    if initial_schedule[position] == new_exercise:
                        initial_schedule[position] = "0"
                initial_schedule.insert(index + 1, new_exercise)
            while "0" in initial_schedule:
                initial_schedule.remove("0")

    elif action == "Exercise":
        if lesson_title in initial_schedule:
            exercise_index = initial_schedule.index(lesson_title) + 1
            if exercise not in initial_schedule:
                initial_schedule.insert(exercise_index, exercise)
        else:
            initial_schedule.append(lesson_title)
            initial_schedule.append(exercise)

for index in range(len(initial_schedule)):
    print(f"{index + 1}.{initial_schedule[index]}")

# test inputs:

# Data Types, Objects, Lists
# Add:Databases
# Insert:Arrays:0
# Remove:Lists
# course start

# Arrays, Lists, Methods
# Swap:Arrays:Methods
# Exercise:Databases
# Swap:Lists:Databases
# Insert:Arrays:0
# course start
