tournament_phase = input()
ticket_type = input()
ticket_count = int(input())
trophy_photo = input()
total_price = 0
ticket_price = 0
if tournament_phase == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    else:
        ticket_price = 118.90
elif tournament_phase == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    else:
        ticket_price = 300.40
else:
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    else:
        ticket_price = 400

total_price = ticket_price * ticket_count
if trophy_photo == "Y":
    if total_price > 4000:
        total_price *= 0.75
    elif total_price > 2500:
        total_price *= 0.90
        total_price += ticket_count * 40
    else:
        total_price += ticket_count * 40
else:
    if total_price > 4000:
        total_price *= 0.75
    elif total_price > 2500:
        total_price *= 0.90
    else:
        pass

print(f"{total_price:.2f}")

# test input Final Premium 25 Y
# test input Semi final VIP 9 Y
# test input Quarter final Standard 11 N
