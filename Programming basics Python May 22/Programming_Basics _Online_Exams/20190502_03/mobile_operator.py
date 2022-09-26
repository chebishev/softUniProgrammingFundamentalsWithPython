contract_time = input()
contract_type = input()
mobile_internet = input()
pay_months = int(input())
price_per_month = 0
if contract_time == "one":
    if contract_type == "Small":
        price_per_month = 9.98
    elif contract_type == "Middle":
        price_per_month = 18.99
    elif contract_type == "Large":
        price_per_month = 25.98
    else:
        price_per_month = 35.99
else:
    if contract_type == "Small":
        price_per_month = 8.58
    elif contract_type == "Middle":
        price_per_month = 17.09
    elif contract_type == "Large":
        price_per_month = 23.59
    else:
        price_per_month = 31.79

if mobile_internet == "yes":
    if price_per_month <= 10:
        price_per_month += 5.50
    elif price_per_month <= 30:
        price_per_month += 4.35
    else:
        price_per_month += 3.85

total = price_per_month * pay_months
if contract_time == "two":
    total *= 0.9625

print(f"{total:.2f} lv.")

# test input one Small yes 10
# test input two Large no 10
# test input two ExtraLarge yes 20
# test input two Small yes 20
