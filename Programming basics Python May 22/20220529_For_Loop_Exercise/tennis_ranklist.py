from math import floor

competitions = int(input())
starting_points = int(input())
points = 0
win_count = 0
semi_final_count = 0
final_count = 0

for numbers in range(competitions):
    tournament_exit = input()
    if tournament_exit == "W":
        points += 2000
        win_count += 1
    elif tournament_exit == "F":
        points += 1200
        final_count += 1
    else:
        points += 720
        semi_final_count += 1

print(f"Final points: {starting_points + points}")
print(f'Average points: {floor(points / competitions)}')
print(f'{((win_count / competitions) * 100):.2f}%')

# test input 5 1400 F SF W W SF
# test input 4 750 SF W SF W
