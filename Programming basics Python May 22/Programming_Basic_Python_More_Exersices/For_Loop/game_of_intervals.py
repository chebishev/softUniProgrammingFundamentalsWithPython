number_of_plays = int(input())
total_result = 0
first_group = 0
second_group = 0
third_group = 0
fourth_group = 0
fifth_group = 0
invalid_numbers = 0

for numbers in range(number_of_plays):
    random_number = int(input())

    if 0 <= random_number <= 9:
        first_group += 1
        total_result += random_number * 0.20
    elif 10 <= random_number <= 19:
        second_group += 1
        total_result += random_number * 0.30
    elif 20 <= random_number <= 29:
        third_group += 1
        total_result += random_number * 0.40
    elif 30 <= random_number <= 39:
        fourth_group += 1
        total_result += 50
    elif 40 <= random_number <= 50:
        fifth_group += 1
        total_result += 100
    else:
        invalid_numbers += 1
        total_result /= 2

first_group_percent = first_group / number_of_plays * 100
second_group_percent = second_group / number_of_plays * 100
third_group_percent = third_group / number_of_plays * 100
fourth_group_percent = fourth_group / number_of_plays * 100
fifth_group_percent = fifth_group / number_of_plays * 100
invalid_numbers_percent = invalid_numbers / number_of_plays * 100

print(f'{total_result:.2f}')
print(f'From 0 to 9: {first_group_percent:.2f}%')
print(f'From 10 to 19: {second_group_percent:.2f}%')
print(f'From 20 to 29: {third_group_percent:.2f}%')
print(f'From 30 to 39: {fourth_group_percent:.2f}%')
print(f'From 40 to 50: {fifth_group_percent:.2f}%')
print(f'Invalid numbers: {invalid_numbers_percent:.2f}%')

# test input 10 43 57 -12 23 12 0 50 40 30 20
