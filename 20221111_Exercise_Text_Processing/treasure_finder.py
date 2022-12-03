# Write a program that decrypts a message by a given key and gathers information about hidden treasure type and its
# coordinates. On the first line, you will receive a key (sequence of numbers separated by a space). On the next few
# lines, you will receive lines with strings until you get the command "find". You should loop through every string
# and decrease the ASCII code of each character with a corresponding number of the key sequence. You choose a key
# number from the sequence by just looping through it. If the length of the key sequence is less than the string
# sequence, you should continue looping from the beginning. For more clarification, see the example below. After
# decrypting the message, you will get a type of treasure and its coordinates. The type will be between the symbol
# "&", and the coordinates - between the symbols "<' and '>'. For each line print the type and the coordinates in the
# format "Found {type} at {coordinates}".

key = list(map(int, input().split()))
while True:

    string = input()
    if string == "find":
        break

    current_key = ""
    char_list = [char for char in string]
    index = 0
    while char_list:
        if index == len(key):
            index = 0
        current_char = char_list.pop(0)
        new_ord_value = ord(current_char) - key[index]
        current_key += chr(new_ord_value)
        index += 1

    resource_type = ""
    coordinates = ""
    resource_found = False
    coordinates_found = False
    for index in range(len(current_key)):
        if current_key[index] == "&":
            if resource_found:
                resource_found = False
                continue
            resource_found = True
            continue
        if current_key[index] == "<":
            coordinates_found = True
            continue
        elif current_key[index] == ">":
            break
        if resource_found:
            resource_type += current_key[index]
        if coordinates_found:
            coordinates += current_key[index]

    print(f"Found {resource_type} at {coordinates}")



# test inputs:

# 1 2 1 3
# ikegfp'jpne)bv=41P83X@
# ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA
# find

# 1 4 2 5 3 2 1
# Ulgwh"jt$ozfj!'kqqg(!bx"A3U237GC
# tsojPqsf$(lrne'$CYfqpshksdvfT$>634O57YC
# 'stj)>34W68Z@
# find
