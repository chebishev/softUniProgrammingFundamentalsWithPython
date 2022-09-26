checkin_minutes = int(input())
checkin_seconds = int(input())
width_in_meters = float(input())
seconds_per_hundred_meters = int(input())

all_seconds = (checkin_minutes * 60) + checkin_seconds
delay = (width_in_meters / 120) * 2.5
trial_time = (width_in_meters / 100) * seconds_per_hundred_meters - delay

if all_seconds >= trial_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {trial_time:.3f}.")
else:
    diff = trial_time - all_seconds
    print(f"No, Marin failed! He was {diff:.3f} second slower.")

# test input 2 12 1200 10
# test input 1 20 1546 12
