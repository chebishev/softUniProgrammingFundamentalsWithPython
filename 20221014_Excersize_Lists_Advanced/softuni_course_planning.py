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
            initial_schedule.insert(len(initial_schedule), lesson_title)

    elif action == "Insert":
        index = int(command[2])
        if lesson_title not in initial_schedule:
            initial_schedule.insert(index, lesson_title)

    elif action == "Remove":
        if lesson_title in initial_schedule:
            initial_schedule.remove(lesson_title)

    elif action == "Swap":
        new_lesson = command[2]
        if lesson_title in initial_schedule:
            current_index = initial_schedule.index(lesson_title)
            initial_schedule[current_index] = new_lesson

    elif action == "Exercise":
        pass

counter = 1
for item in initial_schedule:
    print(f"{counter}. {item}")
    counter += 1
