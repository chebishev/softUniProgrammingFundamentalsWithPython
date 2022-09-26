lucky_number = int(input())

for first_number in range(1, 10):
    for second_number in range(1, 10):
        for third_number in range(1, 10):
            for fourth_number in range(1, 10):
                sum_first_second = first_number + second_number
                sum_third_fourth = third_number + fourth_number
                if sum_third_fourth == sum_first_second and \
                        lucky_number % sum_first_second == 0:
                    print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")
                else:
                    continue

# test input 3
# test input 7
# test input 24
