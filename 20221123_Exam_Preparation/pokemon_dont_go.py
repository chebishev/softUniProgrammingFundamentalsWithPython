import sys

initial_list = list(map(int, input().split()))
total = 0

while initial_list:
    index = int(input())
    current_element = ""
    if index < 0:
        current_element = initial_list.pop(0)
        initial_list.insert(0, initial_list[-1])
    elif index > len(initial_list) - 1:
        current_element = initial_list.pop()
        initial_list.insert(-1, initial_list[0])
    else:
        current_element = initial_list.pop(index)

    for number in initial_list:
        if number <= current_element:
            number += current_element
        else:
            number -= current_element

    total += current_element

print(total)
# it gaves me 12 instead of 14 on the first input

# test inputs:

# 4 5 3
# 1
# 1
# 0

# 5 10 6 3 5
# 2
# 4
# 1
# 1
# 3
# 0
# 0