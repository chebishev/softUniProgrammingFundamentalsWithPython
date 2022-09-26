import sys
max_number = -sys.maxsize
min_number = sys.maxsize

for num in range(0, int(input()), 1):
    temp_number = int(input())

    if temp_number > max_number:
        max_number = temp_number
    if temp_number < min_number:
        min_number = temp_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

# test input 5 10 20 304 0 50
# test input 6 250 5 2 0 100 1000
