numbers_list = input().split()
absolute_list = []
for number in numbers_list:
    current_number = float(number)
    absolute_list.append(abs(current_number))

print(absolute_list)

# test inputs:

# 1 2.5 -3 -4.5

# -0 1 10 -6.66
