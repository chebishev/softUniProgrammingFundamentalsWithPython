game_string = input().split()
total_sum = 0
for item in game_string:
    number = int(item[1:-1:])
    first_letter = item[0]
    last_letter = item[-1]
    if first_letter.isupper():
        total_sum += number / (ord(first_letter) - 64)
    elif first_letter.lower():
        total_sum += number * (ord(first_letter) - 96)
    if last_letter.isupper():
        total_sum -= ord(last_letter) - 64
    elif last_letter.islower():
        total_sum += ord(last_letter) - 96

print(f"{total_sum:.2f}")

# test inputs:

# A12b s17G

# P34562Z q2576f   H456z

# a1A
