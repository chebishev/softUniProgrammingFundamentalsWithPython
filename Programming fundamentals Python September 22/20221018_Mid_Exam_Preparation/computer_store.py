total = 0
is_special = False

while True:
    command = input()

    if command == "special":
        is_special = True
        break
    elif command == "regular":
        break
    else:
        price = float(command)
        if price >= 0:
            total += price
        else:
            print("Invalid price!")
            continue

taxes = total * 0.20
total_price = total + taxes
if total == 0:
    print("Invalid order!")
else:
    if is_special:
        total_price *= 0.90
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total:.2f}$\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")
