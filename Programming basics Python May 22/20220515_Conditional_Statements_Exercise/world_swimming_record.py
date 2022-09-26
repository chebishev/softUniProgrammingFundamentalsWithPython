record_seconds = float(input())
distance = float(input())
time_sec_meter = float(input())

total_time = distance * time_sec_meter

delay = (distance // 15) * 12.5
total_time += delay

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f'No, he failed! He was {(total_time - record_seconds):.2f} seconds slower.')

# test input 10464 1500 20
# test input 55555.67 3017 5.03
