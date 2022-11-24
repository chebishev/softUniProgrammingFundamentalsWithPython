initial_list = input().split(", ")
zero_counter = 0
new_list = []
for item in initial_list:
    if item == "0":
        zero_counter += 1
        continue
    else:
        new_list.append(int(item))

for number in range(zero_counter):
    new_list.append(0)

print(new_list)

# test inputs:

# 1, 0, 1, 2, 0, 1, 3

# 0, 5, 0, 4, 0, 0, 5
