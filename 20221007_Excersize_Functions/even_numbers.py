def even_numbers(numbers):
    return numbers % 2 == 0


list_numbers = input().split()
list_numbers = list(map(int, list_numbers))
even_list = list(filter(even_numbers, list_numbers))
print(even_list)

# test inputs:

# 1 2 3 4

# 1 2 3 -1 -2 -3
