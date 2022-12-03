first_character = ord(input())
second_character = ord(input())
string_to_sum = input()
total = 0
for char in string_to_sum:
    current_ascii = ord(char)
    if first_character < current_ascii < second_character:
        total += current_ascii

print(total)

# test inputs:

# .
# @
# dsg12gr5653feee5

# ?
# E
# @ABCEF
