from math import ceil
from math import floor

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

magnolias_price = magnolias * 3.25
hyacinths_price = hyacinths * 4
roses_price = roses * 3.50
cacti_price = cacti * 8

total_income = magnolias_price + hyacinths_price + roses_price + cacti_price
tax = total_income * 0.05
diff = abs((total_income-tax) - gift_price)

if (total_income-tax) >= gift_price:
    print(f'She is left with {floor(diff)} leva.')
else:
    print(f'She will have to borrow {ceil(diff)} leva.')

# test input 2 3 4 1 50
# test input 15 7 5 10 100
