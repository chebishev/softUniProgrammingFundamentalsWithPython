from math import floor

biscuits_per_day = int(input())
workers_count = int(input())
other_factory_production = int(input())
daily_biscuits = biscuits_per_day * workers_count
total_biscuits = 0
more_biscuits = False

for day in range(1, 31):
    if day % 3 == 0:
        total_biscuits += floor(daily_biscuits * 0.75)
    else:
        total_biscuits += daily_biscuits

print(f"You have produced {total_biscuits} biscuits for the past month.")
factories_difference = 0
if total_biscuits > other_factory_production:
    more_biscuits = True
    factories_difference = total_biscuits - other_factory_production
else:
    factories_difference = other_factory_production - total_biscuits

percent_difference = (factories_difference / other_factory_production) * 100

if more_biscuits:
    print(f"You produce {percent_difference:.2f} percent more biscuits.")
else:
    print(f"You produce {percent_difference:.2f} percent less biscuits.")

# test inputs:

# 78
# 8
# 16000

# 65
# 12
# 26000

# 163
# 16
# 67020