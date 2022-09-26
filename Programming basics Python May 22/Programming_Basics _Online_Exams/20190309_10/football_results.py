first_match = input()
second_match = input()
third_match = input()
win_counter = 0
lose_counter = 0
draw_counter = 0

if first_match[0] > first_match[2]:
    win_counter += 1
elif first_match[0] < first_match[2]:
    lose_counter += 1
else:
    draw_counter += 1

if second_match[0] > second_match[2]:
    win_counter += 1
elif second_match[0] < second_match[2]:
    lose_counter += 1
else:
    draw_counter += 1

if third_match[0] > third_match[2]:
    win_counter += 1
elif third_match[0] < third_match[2]:
    lose_counter += 1
else:
    draw_counter += 1

print(f"Team won {win_counter} games.")
print(f"Team lost {lose_counter} games.")
print(f"Drawn games: {draw_counter}")

# test input 3:1 0:2 0:0
# test input 4:2 0:3 1:0
# test input 0:2 0:1 3:3
