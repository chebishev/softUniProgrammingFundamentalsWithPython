def add_stop(initial_string, position, new):
    initial_string = initial_string[0:position] + new + initial_string[position:]
    return initial_string


def remove_stop(initial_string, start, end):
    initial_string = initial_string.replace(initial_string[start:end+1], "")
    return initial_string


def switch(initial_string, old, new):
    if old in initial_string:
        initial_string = initial_string.replace(old, new)
    return initial_string


def is_valid(initial_string, position, string_start):
    if string_start <= position < len(initial_string):
        return True


all_stops = input()

while True:

    command = input().split(":")
    if command[0] == "Travel":
        break

    action = command[0]

    if action == "Add Stop":
        index = int(command[1])
        string = command[2]
        if is_valid(all_stops, index, 0):
            all_stops = add_stop(all_stops, index, string)

    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if is_valid(all_stops, start_index, 0) and \
                is_valid(all_stops, end_index, start_index):
            all_stops = remove_stop(all_stops, start_index, end_index)

    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        all_stops = switch(all_stops, old_string, new_string)

    print(all_stops)

print(f"Ready for world tour! Planned stops: {all_stops}")

# test inputs:

# Hawai::Cyprys-Greece
# Add Stop:7:Rome
# Remove Stop:11:16
# Switch:Hawai:Bulgaria
# Travel

# Albania:Bulgaria:Cyprus:Deuchland
# Add Stop:3:Nigeria
# Remove Stop:4:8
# Switch:Albania: Azərbaycan
# Travel

