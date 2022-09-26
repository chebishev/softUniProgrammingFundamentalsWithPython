desired_profit = float(input())
command = input()
total = 0
while command != "Party!":
    cocktail_name = command
    cocktails_count = int(input())
    price = len(cocktail_name)
    order = price * cocktails_count
    if order % 2 != 0:
        order *= 0.75
    total += order
    if total >= desired_profit:
        print("Target acquired.")
        break
    command = input()
    if command == "Party!":
        diff = desired_profit - total
        print(f"We need {diff:.2f} leva more.")
        break
print(f"Club income - {total:.2f} leva.")

# test input 500 Bellini 6 Bamboo 7 Party!
# test input 100 Sidecar 7 Mojito 5 White Russian 10
