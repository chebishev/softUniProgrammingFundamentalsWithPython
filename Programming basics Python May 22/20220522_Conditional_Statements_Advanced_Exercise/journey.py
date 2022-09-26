budget = float(input())
season = input()
destination = ''
vacation_type = ''
costs = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        costs = budget * 0.30
        vacation_type = "Camp"
    else:
        costs = budget * 0.70
        vacation_type = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        costs = budget * 0.40
        vacation_type = "Camp"
    else:
        costs = budget * 0.80
        vacation_type = "Hotel"
else:
    destination = "Europe"
    costs = budget * 0.90
    vacation_type = "Hotel"

print(f"Somewhere in {destination}")
print(f'{vacation_type} - {costs:.2f}')

# test input 50 summer
# test input 75 winter
# test input 312 summer
# test input 678.53 winter
# test input 1500 summer
