flower_type = input()
flowers_count = int(input())
budget = int(input())
total = 0

if flower_type == "Roses":
    if flowers_count > 80:
        total = (flowers_count * 5) * 0.90
    else:
        total = flowers_count * 5
elif flower_type == "Dahlias":
    if flowers_count > 90:
        total = (flowers_count * 3.80) * 0.85
    else:
        total = flowers_count * 3.80
elif flower_type == "Tulips":
    if flowers_count > 80:
        total = (flowers_count * 2.80) * 0.85
    else:
        total = flowers_count * 2.80
elif flower_type == "Narcissus":
    if flowers_count < 120:
        total = (flowers_count * 3) * 1.15
    else:
        total = flowers_count * 3
else:
    if flowers_count < 80:
        total = (flowers_count * 2.50) * 1.20
    else:
        total = flowers_count * 2.50

diff = abs(budget - total)

if budget >= total:
    print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')

# test input Roses 55 250
# test input Tulips 88 260
# test input Roses Narcissus 119 360
