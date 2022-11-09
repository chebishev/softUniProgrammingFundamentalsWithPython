import sys
number_of_snowballs = int(input())
highest_value = -sys.maxsize
weight = 0
time_needed = 0
quality = 0
for snowball in range(number_of_snowballs):
    current_weight = int(input())
    current_time_needed = int(input())
    current_quality = int(input())
    result = int((current_weight / current_time_needed) ** current_quality)
    if result > highest_value:
        highest_value = result
        weight = current_weight
        time_needed = current_time_needed
        quality = current_quality

print(f"{weight} : {time_needed} = {highest_value} ({quality})")

# test inputs:

# 2
# 10
# 2
# 3
# 5
# 5
# 5

# 3
# 10
# 5
# 7
# 16
# 4
# 2
# 20
# 2
# 2
