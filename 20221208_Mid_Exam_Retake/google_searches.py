income_per_user = float(input())
number_of_users = int(input())
total_money = 0

for index in range(1, number_of_users + 1):
    number_of_searches = int(input())
    money_per_search = number_of_searches * income_per_user
    if index % 3 == 0:
        money_per_search = number_of_searches * income_per_user * 3
    if number_of_searches > 5:
        total_money += money_per_search * 2
    elif number_of_searches == 1:
        continue
    else:
        total_money += money_per_search

print(f"Total money earned: {total_money:.2f}")

# test inputs:

# 5.5
# 3
# 1
# 10
# 5

# 0.5
# 6
# 3
# 5
# 16
# 0
# 6
# 1

# 3.0
# 7
# 0
# 1
# 2
# 3
# 4
# 6
# 15
