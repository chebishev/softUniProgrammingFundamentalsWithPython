time_for_shooting = int(input())
scenes_count = int(input())
time_per_scene = int(input())
preparation_time = time_for_shooting * 0.15

total_time = scenes_count * time_per_scene + preparation_time
diff = abs(total_time - time_for_shooting)
if total_time <= time_for_shooting:
    print(f"You managed to finish the movie on time! You have {diff:.0f} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {diff:.0f} minutes.")

# test input 120 10 11
# test input 60 15 3
