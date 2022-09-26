pairs_count = int(input())
first_number = 0
second_number = 0
third_number = 0
fourth_number = 0

first_sum = 0
second_sum = 0
diff = 0
max_diff = 0
equal_sum = True

for numbers in range(pairs_count):
    if numbers % 2 == 0:
        first_number = int(input())
        second_number = int(input())
        first_sum = first_number + second_number
    else:
        third_number = int(input())
        fourth_number = int(input())
        second_sum = third_number + fourth_number

    if pairs_count == 1:
        break
    if numbers > 1:
        if first_sum != second_sum:
            equal_sum = False
            diff = abs(first_sum - second_sum)
            if max_diff < diff:
                max_diff = diff
        else:
            equal_sum = True
    else:
        if first_sum != second_sum:
            equal_sum = False
            max_diff = abs(second_sum - first_sum)
        else:
            equal_sum = True

if equal_sum:
    print(f"Yes, value={first_number + second_number}")
else:
    print(f'No, maxdiff={max_diff}')

# test input 3 1 2 0 3 4 -1
# test input 4 1 1 3 1 2 2 0 0
# test input 2 -1 0 0 -1
# test input 2 1 2 2 2
# test input 1 5 5
# test input 2 -1 2 0 -1
