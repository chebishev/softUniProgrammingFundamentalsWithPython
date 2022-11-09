def int_to_str(list_to_transform):
    list_of_strings = [str(number) for number in list_to_transform]
    return ", ".join(list_of_strings)


numbers_list = list(map(int, input().split(", ")))
positive = []
negative = []
even = []
odd = []
for number in numbers_list:
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(f"Positive: {int_to_str(positive)}")
print(f"Negative: {int_to_str(negative)}")
print(f"Even: {int_to_str(even)}")
print(f"Odd: {int_to_str(odd)}")

# test inputs:

# 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33

# 1, 2, 54, 2, 21
