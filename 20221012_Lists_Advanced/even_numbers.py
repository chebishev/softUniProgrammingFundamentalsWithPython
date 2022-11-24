numbers = list(map(int, input().split(", ")))
even_numbers = []
for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        even_numbers.append(index)
print(even_numbers)

# test inputs:

# 3, 2, 1, 5, 8

# 2, 4, 6, 9, 10
