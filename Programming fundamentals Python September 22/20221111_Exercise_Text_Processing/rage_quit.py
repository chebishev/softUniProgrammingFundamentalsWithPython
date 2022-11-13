def out_of_index(lst):
    if len(lst) == 0:
        return True
    return False


rage_input = [char for char in input()]
symbols = ""
numbers = ""
unique_symbols = ""
rage_quit = ""
while True:
    while not rage_input[0].isdigit():
        symbols += rage_input.pop(0).upper()
    while rage_input[0].isdigit():
        numbers += rage_input.pop(0)
        if out_of_index(rage_input):
            break
    rage_quit += symbols * int(numbers)
    symbols = ""
    numbers = ""
    if out_of_index(rage_input):
        break
for char in rage_quit:
    if char not in unique_symbols:
        unique_symbols += char
print(f"Unique symbols used: {len(unique_symbols)}")
print(rage_quit)

# test inputs:

# a3

# aSd2&5s@1
