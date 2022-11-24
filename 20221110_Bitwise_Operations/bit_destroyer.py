dec_to_bin_number = bin(int(input()))
position_to_change = -int(input()) - 1

dec_to_bin_number = [char for char in dec_to_bin_number]
dec_to_bin_number[position_to_change] = "0"

new_number = ""
for char in dec_to_bin_number:
    new_number += char

new_number = int(new_number, 2)
print(new_number)

# test inputs:

# 1313
# 5

# 231
# 2

# 111
# 6

# 111
# 4
