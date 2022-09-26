chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
total = 0
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if season == "Spring" or \
        season == "Summer":
    chrysanthemums_price = chrysanthemums * 2.00
    roses_price = roses * 4.10
    tulips_price = tulips * 2.50
else:
    chrysanthemums_price = chrysanthemums * 3.75
    roses_price = roses * 4.50
    tulips_price = tulips * 4.15

total = chrysanthemums_price + roses_price + tulips_price

if holiday == "Y":
    total *= 1.15

if season == "Spring" and tulips > 7:
    total *= 0.95

if season == "Winter" and roses >= 10:
    total *= 0.90

if chrysanthemums + roses + tulips > 20:
    total *= 0.80

print(f'{(total + 2):.2f}')

# test input 2 4 8 Spring Y
# test input 3 10 9 Winter N
# test input 10 10 10 Autumn N
