number_of_strings = int(input())
key_word = input()
strings_list = []
softuni_list = []
for number in range(number_of_strings):
    current_string = input()
    strings_list.append(current_string)
    if key_word in current_string:
        softuni_list.append(current_string)

print(strings_list)
print(softuni_list)

# test inputs:

# 3
# SoftUni
# I study at SoftUni
# I walk to work
# I learn Python at SoftUni

# 4
# tomatoes
# I love tomatoes
# I can eat tomatoes forever
# I don't like apples
# Yesterday I ate two tomatoes
