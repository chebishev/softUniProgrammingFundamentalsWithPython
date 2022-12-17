concert_dict = {}
while True:

    command = input()
    if command == "Start!":
        break

    command = command.split("; ")
    action = command[0]
    band_name = command[1]
    rest_data = command[2].split(", ")
    if action == "Add":
        if band_name not in concert_dict.keys():
            concert_dict[band_name] = {"members": [], "time": 0}
        for member in rest_data:
            if member not in concert_dict[band_name]["members"]:
                concert_dict[band_name]["members"].append(member)
    elif action == "Play":
        time = int(rest_data[0])
        if band_name not in concert_dict.keys():
            concert_dict[band_name] = {"members": [], "time": 0}
        concert_dict[band_name]["time"] += time
total_time = 0
for key in concert_dict.keys():
    total_time += concert_dict[key]["time"]
print(f"Total time: {total_time}")
for key in concert_dict.keys():
    print(f"{key} -> {concert_dict[key]['time']}")
for key in concert_dict.keys():
    print(key)
    for member in concert_dict[key]["members"]:
        print(f"=> {member}")
    break

# Play; The Beatles; 2584
# Add; The Beatles; John Lennon, George Harrison, Ringo Starr
# Add; The Beatles; Paul McCartney, George Harrison
# Add; The Rolling Stones; Brian Jones, Mick Jagger, Keith Richards
# Play; The Rolling Stones; 4239
# Start!

# Add; The Beatles; John Lennon, Paul McCartney
# Add; The Beatles; Paul McCartney, George Harrison
# Add; The Beatles; George Harrison, Ringo Starr
# Play; The Beatles; 3698
# Play; The Beatles; 3828
# Start!
