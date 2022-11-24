numbers_count = int(input())
positive_list = []
negative_list = []

for number in range(numbers_count):
    current_number = int(input())
    if current_number < 0:
        negative_list.append(current_number)
    else:
        positive_list.append(current_number)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")

# test inputs:

# 5
# 10
# 3
# 2
# -15
# -4

# 6
# 11
# 2
# 35
# 599
# 31
# 20
