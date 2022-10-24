money_list = input().split(", ")
number_of_beggars = int(input())
sum_for_each_beggar = []
current_sum = 0
start_index = 0
for beggar in range(number_of_beggars):
    for number in range(start_index, len(money_list), number_of_beggars):
        current_sum += int(money_list[number])
    sum_for_each_beggar.append(current_sum)
    current_sum = 0
    start_index += 1

print(sum_for_each_beggar)

# test inputs:

# 1, 2, 3, 4, 5
# 2

# 3, 4, 5, 1, 29, 4
# 6

# 100, 94, 24, 99
# 5
