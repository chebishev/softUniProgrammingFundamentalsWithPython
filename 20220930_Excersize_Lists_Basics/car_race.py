cars_times = list(map(int, input().split()))
left_car_time = 0
right_car_time = 0
right_step = -1
for number in range(len(cars_times)//2):
    left_car_time += cars_times[number]
    if cars_times[number] == 0:
        left_car_time *= 0.80
    right_car_time += cars_times[right_step]
    if cars_times[right_step] == 0:
        right_car_time *= 0.80
    right_step -= 1

if left_car_time > right_car_time:
    print(f"The winner is right with total time: {right_car_time:.1f}")
else:
    print(f"The winner is left with total time: {left_car_time:.1f}")