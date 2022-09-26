command = input()
win_counter = 0
lose_counter = 0
total_matches = 0

while command != "End of tournaments":
    tournament_name = command
    matches = int(input())
    for match in range(1, matches + 1):
        home_points = int(input())
        guest_points = int(input())
        total_matches += 1
        diff = abs(home_points - guest_points)
        if home_points > guest_points:
            win_counter += 1
            print(f"Game {match} of tournament {tournament_name}: win with {diff} points.")
        else:
            lose_counter += 1
            print(f"Game {match} of tournament {tournament_name}: lost with {diff} points.")
    command = input()
    if command == "End of tournaments":
        win_percentage = win_counter / total_matches * 100
        lose_percentage = lose_counter / total_matches * 100
        print(f"{win_percentage:.2f}% matches win")
        print(f"{lose_percentage:.2f}% matches lost")
        break

# test inputs:

# Dunkers
# 2
# 75
# 65
# 56
# 73
# Fire Girls
# 3
# 67
# 34
# 83
# 98
# 66
# 45
# End of tournaments

# Ballers
# 3
# 87
# 63
# 56
# 65
# 75
# 64
# Sharks
# 4
# 64
# 76
# 65
# 86
# 68
# 99
# 45
# 78
# End of tournaments
