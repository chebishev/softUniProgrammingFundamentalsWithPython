from math import ceil
from math import floor

days_count = int(input())
food_in_kg = int(input())
dog_food_day_kg = float(input())
cat_food_day_kg = float(input())
turtle_foot_day_kg = float(input()) / 1000

total_needed_food = (dog_food_day_kg + cat_food_day_kg + turtle_foot_day_kg) * days_count
diff = abs(total_needed_food - food_in_kg)

if total_needed_food > food_in_kg:
    print(f'{ceil(diff)} more kilos of food are needed.')
else:
    print(f'{floor(diff)} kilos of food left.')


# test input 2 10 1 1 1200
# test input 5 10 2.1 0.8 321
