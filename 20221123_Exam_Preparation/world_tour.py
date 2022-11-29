all_stops = input()

while True:

    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {all_stops}")
        break

    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(all_stops):
            all_stops = all_stops[:index] + string + all_stops[index:]
            print(all_stops)
        else:
            print(all_stops)

    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(all_stops) and start_index <= end_index < len(all_stops):
            string_to_cut = all_stops[start_index:end_index + 1]
            all_stops = all_stops.replace(string_to_cut, "")
            print(all_stops)
        else:
            print(all_stops)

    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
            print(all_stops)
        else:
            print(all_stops)

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
