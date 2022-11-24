numbers_count = int(input())
even = []
odd = []
negative = []
positive = []

for number in range(numbers_count):
    current_number = int(input())
    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)
    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

command = input()
print(locals()[command])

# test inputs:

# 5
# 33
# 19
# -2
# 18
# 998
# even

# 3
# 111
# -4
# 0
# negative
