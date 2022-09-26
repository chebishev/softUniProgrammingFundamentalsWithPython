joinery_count = int(input())
joinery_type = input()
delivery_option = input()  # 60lv.
price = 0

if joinery_count < 10:
    print("Invalid order")
else:
    if joinery_type == "90X130":
        price = 110
        if 30 < joinery_count <= 60:
            price *= 0.95
        elif joinery_count > 60:
            price *= 0.92
    elif joinery_type == "100X150":
        price = 140
        if 40 < joinery_count <= 80:
            price *= 0.94
        elif joinery_count > 80:
            price *= 0.90
    elif joinery_type == "130X180":
        price = 190
        if 20 < joinery_count <= 50:
            price *= 0.93
        elif joinery_count > 50:
            price *= 0.88
    else:
        price = 250
        if 25 < joinery_count <= 50:
            price *= 0.91
        elif joinery_count > 50:
            price *= 0.86

    total = price * joinery_count

    if delivery_option == "With delivery":
        total += 60

    if joinery_count > 99:
        total *= 0.96

    print(f"{total:.2f} BGN")

# test input 40 90X130 Without delivery
# test input 105 100X150 With delivery
# test input 2 130X180 With delivery
