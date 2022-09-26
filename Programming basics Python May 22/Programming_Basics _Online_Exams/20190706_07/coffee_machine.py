drink_type = input()
add_sugar = input()
drinks_count = int(input())
price = 0

if add_sugar == "Normal":
    if drink_type == "Espresso":
        price = 1
    elif drink_type == "Cappuccino":
        price = 1.20
    else:
        price = 0.60
elif add_sugar == "Extra":
    if drink_type == "Espresso":
        price = 1.20
    elif drink_type == "Cappuccino":
        price = 1.60
    else:
        price = 0.70
else:
    if drink_type == "Espresso":
        price = 0.90
    elif drink_type == "Cappuccino":
        price = 1
    else:
        price = 0.50
    price *= 0.65

if drink_type == "Espresso":
    if drinks_count >= 5:
        price *= 0.75

total = drinks_count * price
if total > 15:
    total *= 0.80

print(f"You bought {drinks_count} cups of {drink_type} for {total:.2f} lv.")

# test input Espresso Without 10
# test input Cappuccino Normal 13
# test input Tea Extra 3
