player_name = input()
total_points = 301
successful_shots = 0
unsuccessful_shots = 0
command = input()
while command != "Retire":
    points_operation = command
    points = int(input())

    if points_operation == "Single":
        if points > total_points:
            unsuccessful_shots += 1
        else:
            total_points -= points
            successful_shots += 1
    elif points_operation == "Double":
        points *= 2
        if points > total_points:
            unsuccessful_shots += 1
        else:
            total_points -= points
            successful_shots += 1
    else:
        points *= 3
        if points > total_points:
            unsuccessful_shots += 1
        else:
            total_points -= points
            successful_shots += 1
    if total_points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break
    command = input()
    if command == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break
# test inputs
# Michael van Gerwen
# Triple
# 20
# Triple
# 19
# Double
# 10
# Single
# 3
# Single
# 1
# Triple
# 20
# Triple
# 20
# Double
# 20

# Stephen Bunting
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Double
# 7
# Single
# 12
# Double
# 1
# Single
# 1

# Rob Cross
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Double
# 20
# Triple
# 20
# Double
# 5
# Triple
# 10
# Double
# 6
# Retire