budget = float(input())
season = input()
category = ""
car_type = ""
price = 0

if budget <= 100:
    category = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.35
    else:
        car_type = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    category = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.45
    else:
        car_type = "Jeep"
        price = budget * 0.80
else:
    category = "Luxury class"
    car_type = "Jeep"
    price = budget * 0.90

print(category)
print(f'{car_type} - {price:.2f}')

# test input 450 Summer
# test input 450 Winter
# test input 99.99 Summer
# test input 70.50 Winter
# test input 1010 Summer
# test input 1010 Winter
