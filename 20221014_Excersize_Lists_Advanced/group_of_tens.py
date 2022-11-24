initial_list = list(map(int, input().split(", ")))
max_value_for_group = 10

while len(initial_list) != 0:
    current_list = []
    for index, value in enumerate(initial_list):
        if value <= max_value_for_group:
            current_list.append(initial_list.pop(index))
            initial_list.insert(index, 0)
    print(f'Group of {max_value_for_group}\'s: {current_list}')
    initial_list = [number for number in initial_list if number != 0]
    if len(initial_list) == 0:
        break
    max_value_for_group += 10

# test inputs:

# 8, 12, 38, 3, 17, 19, 25, 35, 50

# 1, 3, 3, 4, 34, 35, 25, 21, 33
