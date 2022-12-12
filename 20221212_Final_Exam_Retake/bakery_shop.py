bakery_shop = {}
sell_counter = 0

while True:
    command = input()

    if command == "Complete":
        break

    action, quantity, food = command.split()
    quantity = int(quantity)

    if action == "Receive":
        if food not in bakery_shop.keys():
            if quantity > 0:
                bakery_shop[food] = quantity

    elif action == "Sell":
        if food not in bakery_shop.keys():
            print(f"You do not have any {food}.")
        elif quantity > bakery_shop[food]:
            current_quantity = bakery_shop[food]
            print(f"There aren't enough {food}. You sold the last {current_quantity} of them.")
            del bakery_shop[food]
            sell_counter += current_quantity
        else:
            bakery_shop[food] -= quantity
            print(f"You sold {quantity} {food}.")
            if bakery_shop[food] == 0:
                del bakery_shop[food]
            sell_counter += quantity

for key, value in bakery_shop.items():
    print(f"{key}: {value}")

print(f"All sold: {sell_counter} goods")

# test inputs:

# Receive 105 cookies
# Receive 10 donuts
# Sell 10 donuts
# Sell 1 bread
# Complete

# Receive 10 muffins
# Receive 23 bagels
# Sell 5 muffins
# Sell 10 bagels
# Complete
