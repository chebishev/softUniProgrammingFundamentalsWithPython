rage_input = [char for char in input()]
symbols = ""
numbers = ""
unique_symbols = ""
rage_quit = ""
while True:
    while not rage_input[0].isdigit():
        symbols += rage_input.pop(0).upper()
        if len(rage_input) == 0:
            break
    while rage_input[0].isdigit():
        numbers += rage_input.pop(0)
        if len(rage_input) == 0:
            break
    rage_quit += symbols * int(numbers)
    symbols = ""
    numbers = ""
    if len(rage_input) == 0:
        break
for char in rage_quit:
    if char not in unique_symbols:
        unique_symbols += char
print(f"Unique symbols used: {len(unique_symbols)}")
print(rage_quit)

# test inputs:

# a3

# aSd2&5s@1
