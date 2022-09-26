strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price * 0.50
oranges_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20

strawberries = strawberries_kg * strawberries_price
bananas = bananas_kg * bananas_price
raspberries = raspberries_kg * raspberries_price
oranges = oranges_kg * oranges_price

total = strawberries + bananas + oranges + raspberries

print(f"{total:.2f}")

# test input 48 10 3.3 6.5 1.7
# test input 63.5 3.57 6.35 8.15 2.5
