budget = float(input())
season = input()
location = ""
place = ""
price = 0

if season == "Summer":
    location = "Alaska"
    if budget <= 1000:
        place = "Camp"
        price = budget * 0.65
    elif 1000 < budget <= 3000:
        place = "Hut"
        price = budget * 0.80
    else:
        place = "Hotel"
else:
    location = "Morocco"
    if budget <= 1000:
        place = "Camp"
        price = budget * 0.45
    elif 1000 < budget <= 3000:
        place = "Hut"
        price = budget * 0.60
    else:
        place = "Hotel"

if place == "Hotel":
    price = budget * 0.90

print(f'{location} - {place} - {price:.2f}')

# test input 800 Summer
# test input 799.50 Winter
# test input 3460 Summer
# test input 1100 Summer
# test input 5000 Winter
# test input 2453.99 Winter
