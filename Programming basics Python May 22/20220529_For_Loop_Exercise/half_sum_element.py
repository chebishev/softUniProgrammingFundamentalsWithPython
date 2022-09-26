import sys

count_numbers = int(input())
max_num = -sys.maxsize
total = 0

for numbers in range(count_numbers):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number

    total += current_number

if total - max_num == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    total = total - max_num
    print(f"Diff = {abs(total - max_num)}")

# test input 7 3 4 1 1 2 12 1
# test input 4 6 1 2 3
# test input 3 1 1 10
# test input 3 5 5 1
# test input 3 111
