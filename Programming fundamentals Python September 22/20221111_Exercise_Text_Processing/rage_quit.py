# initial string
quit_string = input()

# dictionary whose keys will be string parts before number, and values - number (for multiplication)
quit_dict = {}

symbols = ""  # current symbols holder
numbers = ""  # current numbers holder

# looping through every character in the string
for character in quit_string:
    if character.isdigit():  # check if character is digit
        # if there is data in numbers or symbols variables, the digit is the second one
        if len(numbers) == 1 and len(symbols):
            numbers += character  # adding the second (i hope) digit to numbers
            quit_dict[symbols] = int(numbers)  # adding the current symbols and the number as key/value in the dict

            # resetting the variables
            numbers = ""
            symbols = ""

        else:  # if no data in numbers: append the current digit
            numbers += character

    else:  # the character is not digit
        if len(numbers) == 0:  # if no digits in numbers is the time to push some characters
            symbols += character  # append the character to the string
        else:  # if digit(s) in number we are already on characters so add the digits as value in the key
            quit_dict[symbols] = int(numbers)
            numbers = ""  # reset the variable
            symbols = character  # reset the variable and set new character as initial value

# Now we are out of the loop so if there is something valid in the variables - add it to the dictionary
if len(symbols) or len(numbers):
    quit_dict[symbols] = int(numbers)

# declaring empty dictionary in order to use all characters as unique keys
unique_symbols = {}

# this will be printed at the final
final_string = ""

# looping through the keys and multiplicate them with the int(values)
for key in quit_dict.keys():
    if not quit_dict[key] == 0:
        final_string += key * quit_dict[key]
    else:
        continue
    # looping through the characters of each key and add them as keys in the unique dictionary
    for symbol in final_string:
        unique_symbols[symbol.upper()] = 0  # obviously with value 0

print(f"Unique symbols used: {len(unique_symbols)}")  # counting the unique values
print(final_string.upper())  # printing the string with upper case

# 85/100 judge
# test inputs:

# a3

# aSd2&5s@1
