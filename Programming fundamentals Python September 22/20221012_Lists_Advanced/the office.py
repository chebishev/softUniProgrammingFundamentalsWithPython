employees_happiness = list(map(int, input().split(" ")))
improvement_factor = int(input())
multiplied_list = []
counter = 0
average = 0
for index in range(len(employees_happiness)):
    multiplied_list.append(employees_happiness[index] * improvement_factor)

average = sum(multiplied_list) / len(employees_happiness)
for value in multiplied_list:
    if int(value) >= average:
        counter += 1

if counter >= len(employees_happiness) / 2:
    print(f"Score: {counter}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(employees_happiness)}. Employees are not happy!")

# test inputs:

# 1 2 3 4 2 1
# 3

# 2 3 2 1 3 3
# 4
