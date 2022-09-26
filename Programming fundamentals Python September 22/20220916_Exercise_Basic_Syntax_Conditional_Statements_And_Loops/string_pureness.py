number_of_strings = int(input())

for string in range(number_of_strings):
    current_string = input()
    if "," in current_string or \
            "." in current_string or \
            "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")

# test inputs:

# 2
# pure string
# not_pure_string

# 3
# SoftUni
# 12345
# string.pureness