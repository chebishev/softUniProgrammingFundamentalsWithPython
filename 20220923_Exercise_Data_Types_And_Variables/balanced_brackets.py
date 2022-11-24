number_of_lines = int(input())
left_bracket = 0
right_bracket = 0
brackets_counter = 0
balanced_counter = 0
unbalanced_counter = 0

for line in range(number_of_lines):
    current_line = input()
    if ")" in current_line:
        if left_bracket == 0:
            unbalanced_counter += 1
            break
        else:
            brackets_counter += 1
            balanced_counter += 1
            left_bracket = 0
    if "(" in current_line:
        brackets_counter += 1
        if left_bracket > 0:
            unbalanced_counter += 1
            break
        else:
            left_bracket = 1
    else:
        continue
if unbalanced_counter != 0:
    print("UNBALANCED")
elif brackets_counter % 2 != 0:
    print("UNBALANCED")
elif brackets_counter < 2:
    print("UNBALANCED")
else:
    print("BALANCED")

# test inputs:

# (
# 5 + 10
# )
# * 2 +
# (
# 5
# )
# -12


# (
# 5 + 10
# )
# * 2 +
# (
# 5
# )
# -12
