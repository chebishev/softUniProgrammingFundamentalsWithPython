key = int(input())
number_of_lines = int(input())
decrypted_message = ""

for line in range(number_of_lines):
    current_letter = input()
    decrypted_letter = ord(current_letter) + key
    decrypted_message += chr(decrypted_letter)

print(decrypted_message)

# test inputs:

# 3
# 7
# P
# l
# c
# q
# R
# k
# f

# 1
# 7
# C
# d
# b
# q
# x
# o
# s
