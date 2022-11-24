def family(years, km):
    initial_tax = 50
    for year in range(int(years)):
        initial_tax -= 5
    initial_tax += 12 * (int(km) // 3000)
    return initial_tax


def heavy_duty(years, km):
    initial_tax = 80
    for year in range(int(years)):
        initial_tax -= 8
    initial_tax += 14 * (int(km) // 9000)
    return initial_tax


def sports(years, km):
    initial_tax = 100
    for year in range(int(years)):
        initial_tax -= 9
    initial_tax += 18 * (int(km) // 2000)
    return initial_tax


cars_info = input().split(">>")
successful = True
tax = 0
tax_collected = 0

for index in range(len(cars_info)):
    successful = True
    car_type, years_tax, kilometers = cars_info[index].split()

    if car_type == "family":
        tax = family(years_tax, kilometers)

    elif car_type == "heavyDuty":
        tax = heavy_duty(years_tax, kilometers)

    elif car_type == "sports":
        tax = sports(years_tax, kilometers)

    else:
        successful = False
        print("Invalid car type.")
        continue

    tax_collected += tax

    if successful:
        print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {tax_collected:.2f} euros in taxes.")

# test inputs:

# family 3 7210>>van 4 2345>>heavyDuty 9 31000>>sports 4 7410

# family 5 3210>>pickUp 1 1345>>heavyDuty 7 21000>>sports 5 9410>>family 3 9012
