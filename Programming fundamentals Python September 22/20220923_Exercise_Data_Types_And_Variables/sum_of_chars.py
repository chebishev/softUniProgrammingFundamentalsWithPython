number_of_lines = int(input())
result = 0
for char in range(number_of_lines):
    current_char = input()
    result += ord(current_char)

print(f"The sum equals: {result}")

# test inputs:

# 5 A b C d E

# 12 S o f t U n i R u l z z
