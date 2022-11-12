string_for_stripping = input()
output_string = string_for_stripping[0]

for character in range(1, len(string_for_stripping)):
    if string_for_stripping[character] != string_for_stripping[character - 1]:
        output_string += string_for_stripping[character]
    else:
        continue

print(output_string)

# test inputs:

# aaaaabbbbbcdddeeeedssaa

# qqqwerqwecccwd
