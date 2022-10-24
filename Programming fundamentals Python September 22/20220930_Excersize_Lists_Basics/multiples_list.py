factor = int(input())
count = int(input())
final_list = []

for number in range(1, count + 1):
    current_number = number * factor
    final_list.append(current_number)

print(final_list)

# test inputs:

# 2
# 5

# 1
# 10
