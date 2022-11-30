initial_schedule = input().split(", ")

while True:

    command = input()
    if command == "course start":
        break

    command = command.split(":")
    action = command[0]
    lesson_title = command[1]

    if action == "Add":
        if lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)

    elif action == "Insert":
        index = int(command[2])
        if lesson_title not in initial_schedule:
            if 0 <= index <= len(initial_schedule):
                initial_schedule.insert(index, lesson_title)

    elif action == "Remove":
        if lesson_title in initial_schedule:
            initial_schedule.remove(lesson_title)
        exercise = lesson_title + "-Exercise"
        if exercise in initial_schedule:
            initial_schedule.remove(exercise)

    elif action == "Swap":
        new_lesson = command[2]
        exercise = lesson_title + "-Exercise"
        new_exercise = new_lesson + "-Exercise"
        if lesson_title in initial_schedule and new_lesson in initial_schedule:
            index, new_index = initial_schedule.index(lesson_title), initial_schedule.index(new_lesson)
            initial_schedule[index], initial_schedule[new_index] = new_lesson, lesson_title
            if initial_schedule[index + 1] == exercise and initial_schedule[new_index + 1] == new_exercise:
                initial_schedule[index + 1], initial_schedule[new_index + 1] = new_exercise, exercise
            elif initial_schedule[index + 1] == exercise:
                initial_schedule.insert(index, initial_schedule.pop(index + 1))
            elif new_index + 1 < len(initial_schedule):
                if initial_schedule[new_index + 1] == new_exercise:
                    initial_schedule.insert(index + 1, initial_schedule.pop(new_index + 1))

    elif action == "Exercise":
        if lesson_title in initial_schedule:
            exercise = lesson_title + "-Exercise"
            exercise_index = initial_schedule.index(lesson_title) + 1
            if initial_schedule[exercise_index] == exercise:
                continue
            else:
                initial_schedule.insert(exercise_index, exercise)
        else:
            initial_schedule.append(lesson_title)
            exercise = lesson_title + "-Exercise"
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
