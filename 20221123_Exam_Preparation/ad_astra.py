import re
from math import floor

food_information = input()
total_calories = 0
food_list = []
pattern = r"(#|\|)([A-Z a-z]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1([\d]+)\1"
food_date_calories = re.findall(pattern, food_information)
for data in food_date_calories:
    food = data[1]
    date = data[2]
    calories = int(data[3])
    total_calories += calories
    current_string = f"Item: {food}, Best before: {date}, Nutrition: {calories}"
    food_list.append(current_string)

days_to_last = floor(total_calories / 2000)
print(f"You have food to last you for: {days_to_last} days!")
print(f"\n".join(food_list))

# test inputs:

# #Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|

# $$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|

# Hello|#Invalid food#19/03/20#450|$5*(@
