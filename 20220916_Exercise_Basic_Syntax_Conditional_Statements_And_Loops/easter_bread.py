budget = float(input())
price_per_kg_flour = float(input())
eggs_price = price_per_kg_flour * 0.75
milk_price_per_quarter = (price_per_kg_flour * 1.25) / 4
eggs_counter = 0
loaves_counter = 0

while budget >= 0:
    current_bread = price_per_kg_flour + eggs_price + milk_price_per_quarter
    if budget - current_bread < 0:
        break
    else:
        budget -= current_bread
        loaves_counter += 1
        eggs_counter += 3
    if loaves_counter % 3 == 0:
        eggs_counter -= (loaves_counter - 2)

print(f"You made {loaves_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")

# test inputs:

# 20.50
# 1.25

# 15.75
# 1.4
