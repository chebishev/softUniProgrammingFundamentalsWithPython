items_list = input().split("|")
budget = int(input())
bought_items_prices = []
profit = 0.00
new_budget = 0
for item in items_list:
    markup_price = 0
    current_item = item.split("->")
    item_type = current_item[0]
    item_price = float(current_item[1])
    if budget >= item_price:
        if item_type == "Clothes" and item_price <= 50.00 or \
                item_type == "Shoes" and item_price <= 35.00 or \
                item_type == "Accessories" and item_price <= 20.50:
            budget -= item_price
            markup_price = item_price * 1.4
            bought_items_prices.append(f"{markup_price:.2f}")
        else:
            continue
    else:
        continue
    profit += item_price * 0.40
    new_budget += markup_price
print(" ".join(bought_items_prices))
print(f"Profit: {profit:.2f}")
new_budget += budget
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

# test inputs:

# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120

# Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60
# 90
