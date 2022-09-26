fuel_type = input()
fuel_quantity = float(input())
club_card = input()
total = 0

if club_card == "Yes":
    if fuel_type == "Gasoline":
        total = fuel_quantity * 2.04
    elif fuel_type == "Diesel":
        total = fuel_quantity * 2.21
    else:
        total = fuel_quantity * 0.85
else:
    if fuel_type == "Gasoline":
        total = fuel_quantity * 2.22
    elif fuel_type == "Diesel":
        total = fuel_quantity * 2.33
    else:
        total = fuel_quantity * 0.93

if fuel_quantity > 25:
    total = total * 0.90
elif fuel_quantity >= 20:
    total = total * 0.92

print(f'{total:.2f} lv.')

# test input Gas 30 Yes
# test input Gasoline 25 No
# test input Diesel 19 No
