orders = {}

while True:

    command = input()

    if command == "buy":
        break

    name, price, quantity = command.split()

    if name not in orders.keys():
        orders[name] = [0.00, 0]
    orders[name][0] = float(price)
    orders[name][1] += int(quantity)


for key, value in orders.items():
    total = value[0] * value[1]
    print(f"{key} -> {total:.2f}")

# test inputs:

# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy

# Beer 2.40 350
# Water 1.25 200
# IceTea 5.20 100
# Beer 1.20 200
# IceTea 0.50 120
# buy

# CesarSalad 10.20 25
# SuperEnergy 0.80 400
# Beer 1.35 350
# IceCream 1.50 25
# buy
