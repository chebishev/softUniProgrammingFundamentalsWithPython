def add_and_subtract(first, second, third):
    sum_numbers(first, second)
    return subtract(third)


def sum_numbers(first, second):
    return first + second


def subtract(third):
    return sum_numbers(first_number, second_number) - third


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))

# test inputs:

# 23
# 6
# 10

# 1
# 17
# 30

# 42
# 58
# 100
