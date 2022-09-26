from math import ceil
people_count = int(input())
entrance_price = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())

deck_chairs = ceil(people_count * 0.75)
umbrellas = ceil(people_count * 0.5)
total = people_count * entrance_price + deck_chairs * deck_chair_price + umbrellas * umbrella_price

print(f"{total:.2f} lv.")

# test input 21 5.50 4.40 6.20
# test input 50 6 8 4
# test input 100 8 6 4
