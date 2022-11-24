numbers = input().split()
inverted_numbers = []
for element in numbers:
    current_number = -int(element)
    inverted_numbers.append(current_number)
print(inverted_numbers)

# test inputs:

# 1 2 -3 -3 5

# -4 0 2 57 -101
