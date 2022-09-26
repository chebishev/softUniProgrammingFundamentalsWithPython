season = input()
km_per_month = float(input())
salary = 0
km_per_season = km_per_month * 4

if km_per_month <= 5000:
    if season == "Summer":
        salary = km_per_season * 0.90
    elif season == "Winter":
        salary = km_per_season * 1.05
    else:
        salary = km_per_season * 0.75
elif 5000 < km_per_month <= 10000:
    if season == "Summer":
        salary = km_per_season * 1.10
    elif season == "Winter":
        salary = km_per_season * 1.25
    else:
        salary = km_per_season * 0.95
else:
    salary = km_per_season * 1.45

salary *= 0.90

print(f'{salary:.2f}')

# test input Summer 3455
# test input Winter 4350
# test input Spring 1600
# test input Winter 5678
# test input Autumn 8600
# test input Winter 16042
# test input Spring 16942
