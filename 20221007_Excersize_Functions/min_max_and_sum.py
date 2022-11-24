def min_max_and_sum(int_list):
    min_number = min(int_list)
    max_number = max(int_list)
    sum_numbers = sum(int_list)
    return f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_numbers}"


numbers = input().split()
numbers = list(map(int, numbers))
print(min_max_and_sum(numbers))

# test inputs:

# 2 4 6

# 12 52 11 53 2 8 45
