def sort(numbers):
    return sorted(numbers)


unsorted_list = input().split()
unsorted_list = list(map(int, unsorted_list))
print(sort(unsorted_list))

# test inputs:

# 6 2 4

# 12 52 11 53 2 8 45
