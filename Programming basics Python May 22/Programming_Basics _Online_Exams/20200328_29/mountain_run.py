record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_meter = float(input())

slope = distance_in_meters // 50
trial_time = distance_in_meters * time_in_seconds_per_meter + (slope * 30)

diff = trial_time - record_in_seconds

if record_in_seconds <= trial_time:
    print(f"No! He was {diff:.2f} seconds slower.")
else:
    print(f'Yes! The new record is {trial_time:.2f} seconds.')

# test input 10164 1400 25
# test input 5554.36 1340 3.23
