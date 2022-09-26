from math import floor
from math import ceil

field_area = int(input())
grapes_per_square_meter = float(input())
needed_liters = int(input())
workers_count = int(input())

harvest_total = field_area * grapes_per_square_meter
wine = (harvest_total * 0.40) / 2.5

if needed_liters > wine:
    print(f'It will be a tough winter! More {floor(needed_liters - wine)} liters wine needed.')
else:
    diff = wine - needed_liters
    print(f'Good harvest this year! Total wine: {ceil(wine)} liters.')
    print(f'{ceil(diff)} liters left -> {ceil(diff / workers_count)} liters per person.')

# test input 650 2 175 3
# test input 1020 1.5 425 4
