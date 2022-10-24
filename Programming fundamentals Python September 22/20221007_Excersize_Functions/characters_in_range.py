def characters_in_range(first, second):
    list_of_characters = []
    for number in range(first+1, second):
        list_of_characters.append(chr(number))
    return " ".join(list_of_characters)


first_character = ord(input())
second_character = ord(input())
print(characters_in_range(first_character, second_character))

# test inputs:

# a
# d

# #
# :

# #
# C
