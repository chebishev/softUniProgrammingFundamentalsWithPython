month = input()
nights = int(input())
total_studio = 0
total_apartment = 0

if 7 < nights <= 14:
    if month == "May" or \
            month == "October":
        total_studio = (nights * 50) * 0.95
        total_apartment = nights * 65
    elif month == "June" or \
            month == "September":
        total_apartment = nights * 68.70
        total_studio = nights * 75.20
    else:
        total_apartment = nights * 77
        total_studio = nights * 76
elif nights <= 7:
    if month == "May" or \
            month == "October":
        total_studio = nights * 50
        total_apartment = nights * 65
    elif month == "June" or \
            month == "September":
        total_apartment = nights * 68.70
        total_studio = nights * 75.20
    else:
        total_apartment = nights * 77
        total_studio = nights * 76
else:
    if month == "May" or \
            month == "October":
        total_studio = (nights * 50) * 0.70
        total_apartment = (nights * 65) * 0.90
    elif month == "June" or \
            month == "September":
        total_studio = (nights * 75.20) * 0.80
        total_apartment = (nights * 68.70) * 0.90
    else:
        total_studio = nights * 76
        total_apartment = (nights * 77) * 0.90

print(f'Apartment: {total_apartment:.2f} lv.')
print(f'Studio: {total_studio:.2f} lv.')

# test input May 15
# test input June 14
# test input August 20
