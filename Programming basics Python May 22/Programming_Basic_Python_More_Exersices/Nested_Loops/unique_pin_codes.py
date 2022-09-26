first_range = int(input())
second_range = int(input())
third_range = int(input())

for first_number in range(2, first_range + 1, 2):
    for second_number in range(2, second_range+1):
        for third_number in range(2, third_range + 1, 2):
            if second_number == 2 or \
                    second_number == 3 or \
                    second_number == 5 or \
                    second_number == 7:
                print(f"{first_number} {second_number} {third_number}")
            else:
                continue

# test input 3 5 5
# test input 8 2 8