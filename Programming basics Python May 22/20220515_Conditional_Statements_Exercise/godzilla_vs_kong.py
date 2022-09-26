budget = float(input())
statist_count = int(input())
clothing_price = float(input())

decor = budget * 0.10
all_clothes_price = statist_count * clothing_price

if statist_count > 150:
    all_clothes_price = all_clothes_price * 0.90

expenses = decor + all_clothes_price

diff = abs(expenses - budget)

if expenses <= budget:
    print("Action!")
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')

# test input 20000 120 55.5
# test input 15437.62 186 57.99
# test input 9587.88 222 55.69
