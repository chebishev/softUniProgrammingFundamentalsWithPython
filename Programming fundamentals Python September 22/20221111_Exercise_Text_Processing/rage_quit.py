quit_string = input()   # initial string
quit_dict = {}  # dictionary whose keys will be string parts before number, and values - number (for multiplication)
symbols = ""    # current symbols holder
numbers = ""    # current numbers holder
for character in quit_string:   # looped through every character in the string
    if character.isdigit():  # check if character is digit
        if len(numbers) > 0:  # if there is data in numbers or symbols the digit is the second one
            numbers += character  # adding the second (i hope) digit to numbers
            quit_dict[symbols] = int(numbers)  # adding the current symbols and the number as key/value in the dict
            numbers = ""    # resetting the variables
            symbols = ""
        else:       # if no data in numbers: append the current digit
            numbers += character
    else:
        if len(numbers) == 0:  # if no digits in numbers is the time to push some characters
            symbols += character  # append the character to the string
        else:              # if digit(s) in number we are already on characters so add the digits as value in the key
            quit_dict[symbols] = int(numbers)
            numbers = ""  # reset the variable
            symbols = character   # reset the variable and set new character as initial value
# Now we are out of the loop so if there is something valid in the variables - add it to the dictionary
if len(symbols) and len(numbers):
    quit_dict[symbols] = int(numbers)
unique_symbols = {}  # declaring empty dictionary in order to use all characters as unique keys
final_string = ""  # this will be printed at the final
for key in quit_dict.keys():  # looping through the keys and multiplicate them with the int(values)
    final_string += key * int(quit_dict[key])
    for symbol in key: # looping through the characters of each key and add them as keys in the unique dictionary
        unique_symbols[symbol.upper()] = 0  # obviously with value 0
print(f"Unique symbols used: {len(unique_symbols)}")  # counting the unique values
print(final_string.upper())  # printing the string with upper case

# 85/100 judge
# test inputs:

# a3

# aSd2&5s@1

