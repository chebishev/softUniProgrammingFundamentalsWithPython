first_string, second_string = input().split()
total = 0

if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total += ord(first_string[index])
elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total += ord(second_string[index])
else:
    for index in range(len(first_string)):
        total += ord(first_string[index]) * ord(second_string[index])

print(total)
# test inputs:

# George Peter

# 123 522

# a aaaa
