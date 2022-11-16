def tribonacci_sequence(number):
    one_number_back = 1
    two_numbers_back = 0
    three_numbers_back = 0
    output_list = [1]
    for index in range(number - 1):
        current_number = one_number_back + two_numbers_back + three_numbers_back
        three_numbers_back = two_numbers_back
        two_numbers_back = one_number_back
        one_number_back = current_number
        output_list.append(current_number)
    return output_list


number_of_repetitions = int(input())
output = tribonacci_sequence(number_of_repetitions)
print(*output, end=" ")

# test inputs:

# 4

# 8
