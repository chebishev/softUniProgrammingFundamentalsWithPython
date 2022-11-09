plunder_days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0
for day in range(1, plunder_days +1):
    if day % 3 != 0 and day % 5 != 0:
        total_plunder += daily_plunder
    if day % 3 == 0:
        current_plumber = daily_plunder * 1.5
        total_plunder += current_plumber
    if day % 5 == 0:
        if day % 3 == 0:
            total_plunder *= 0.70
        else:
            total_plunder += daily_plunder
            total_plunder *= 0.70
if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")

# test inputs:

# 5
# 40
# 100

# 10
# 20
# 380