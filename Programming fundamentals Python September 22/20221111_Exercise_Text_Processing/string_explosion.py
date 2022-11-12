initial_string = input()
output_string = ""
strength = 0
for index in range(len(initial_string)):
    if strength > 0 and initial_string[index] != ">":
        strength -= 1
    elif initial_string[index] == ">":
        output_string += initial_string[index]
        strength += int(initial_string[index + 1])
    else:
        output_string += initial_string[index]
print(output_string)

# test inputs:

# abv>1>1>2>2asdasd

# pesho>2sis>1a>2akarate>4hexmaster
