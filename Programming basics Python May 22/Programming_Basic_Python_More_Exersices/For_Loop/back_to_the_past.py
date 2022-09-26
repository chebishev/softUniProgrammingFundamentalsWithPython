heritage_money = float(input())
target_year = int(input())
age = 18
needed_money = 0

for numbers in range(1800, target_year+1):
    if numbers % 2 == 0:
        needed_money += 12000
    else:
        needed_money += 12000 + (age * 50)

    age += 1

diff = abs(needed_money-heritage_money)
if needed_money > heritage_money:
    print(f'He will need {diff:.2f} dollars to survive.')
else:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')

# test input 50000 1802
# test input 10000.15 1808
