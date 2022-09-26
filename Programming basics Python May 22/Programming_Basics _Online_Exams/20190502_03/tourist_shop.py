budget = float(input())
command = input()
product_count = 0
total = 0
while command != "Stop":
    product_name = command
    product_price = float(input())
    product_count += 1
    if product_count % 3 == 0:
        product_price *= 0.50

    total += product_price
    if total > budget:
        print("You don't have enough money!")
        print(f"You need {(total-budget):.2f} leva!")
        break
    command = input()
    if command == "Stop":
        print(f"You bought {product_count} products for {total:.2f} leva.")
        break

# test input 153.20 Backpack 25.20 Shoes 54 Sunglasses 30 Stop
# test input 54 Thermal underwear 24 Sunscreen 45
