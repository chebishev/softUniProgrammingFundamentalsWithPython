number = input()
sorted_string = sorted(number)
sorted_number = sorted_string[::-1]
conversion = (str(integer) for integer in sorted_number)
list_to_integer = "".join(conversion)
max_number = int(list_to_integer)
print(max_number)

# test inputs:

# 213

# 7389