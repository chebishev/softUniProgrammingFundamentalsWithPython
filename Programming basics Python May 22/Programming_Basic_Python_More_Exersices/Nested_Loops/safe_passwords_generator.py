range_one = int(input())
range_two = int(input())
max_passwords_count = int(input())
first_letter = 35
second_letter = 64
combinations_counter = 0

for first_number in range(1, range_one + 1):
    if combinations_counter == max_passwords_count:
        break
    for second_number in range(1, range_two + 1):
        if first_letter > 55:
            first_letter = 35
        if second_letter > 96:
            second_letter = 64
        print(f"{chr(first_letter)}{chr(second_letter)}{first_number}{second_number}{chr(second_letter)}{chr(first_letter)}", end="|")
        first_letter += 1
        second_letter += 1
        combinations_counter += 1
        if combinations_counter == max_passwords_count:
            break

# test input 2 3 10
# test input 20 50 10
