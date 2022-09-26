tournaments_count = int(input())
start_points = int(input())
final_points = 0
average_points = 0
win_count = 0
winning_percentage = 0
for tournament in range(tournaments_count):
    phase = input()
    if phase == "W":
        win_count += 1
        final_points += 2000
    elif phase == "F":
        final_points += 1200
    else:
        final_points += 720

average_points = final_points / tournaments_count
final_points += start_points
winning_percentage = win_count / tournaments_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {int(average_points)}")
print(f"{winning_percentage:.2f}%")

# test inputs:

# 5
# 1400
# F
# SF
# W
# W
# SF

# 5
# 1400
# F
# SF
# W
# W
# SF

# 7
# 1200
# SF
# F
# W
# F
# W
# SF
# W