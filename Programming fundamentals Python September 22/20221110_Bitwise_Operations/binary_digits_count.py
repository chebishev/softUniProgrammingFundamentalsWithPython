dec_to_bin_number = bin(int(input()))
bin_for_checking = int(input())
counter = 0

for digit in range(2, len(dec_to_bin_number)):
    if int(dec_to_bin_number[digit]) == bin_for_checking:
        counter += 1

print(counter)

# test inputs:

# 20
# 0

# 15
# 1

# 10
# 0
