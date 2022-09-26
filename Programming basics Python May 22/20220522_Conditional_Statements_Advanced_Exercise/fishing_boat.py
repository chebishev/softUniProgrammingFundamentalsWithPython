budget = int(input())
season = input()
fisherman_count = int(input())
total = 0

if season == "Spring":
    if fisherman_count <= 6:
        total = 3000 * 0.9
    elif 7 <= fisherman_count <= 11:
        total = 3000 * 0.85
    else:
        total = 3000 * 0.75
elif season == "Summer" or season == "Autumn":
    if fisherman_count <= 6:
        total = 4200 * 0.9
    elif 7 <= fisherman_count <= 11:
        total = 4200 * 0.85
    else:
        total = 4200 * 0.75
else:
    if fisherman_count <= 6:
        total = 2600 * 0.9
    elif 7 <= fisherman_count <= 11:
        total = 2600 * 0.85
    else:
        total = 2600 * 0.75

if fisherman_count % 2 == 0 and season != "Autumn":
    total *= 0.95

diff = abs(budget - total)
if budget >= total:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')

# test input 3000 Summer 11
# test input 3600 Autumn 6
# test input 2000 Winter 13
