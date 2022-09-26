days = int(input()) - 1
room_type = input()
rating = input()
total = 0
apartment = days * 25
president_apartment = days * 35

if room_type == "room for one person":
    total = days * 18
elif room_type == "apartment":
    if days < 10:
        total = apartment * 0.70
    elif 10 <= days <= 15:
        total = apartment * 0.65
    else:
        total = apartment * 0.50
else:
    if days < 10:
        total = president_apartment * 0.90
    elif 10 <= days <= 15:
        total = president_apartment * 0.85
    else:
        total = president_apartment * 0.80

if rating == "positive":
    total *= 1.25
else:
    total *= 0.90

print(f'{total:.2f}')

# test input 14 apartment positive
# test input 30 president apartment negative
# test input 12 room for one person positive
