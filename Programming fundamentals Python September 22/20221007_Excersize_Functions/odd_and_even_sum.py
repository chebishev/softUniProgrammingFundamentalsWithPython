def odd_and_even_sum(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in number:
        current_number = int(digit)
        if current_number % 2 == 0:
            sum_of_even_digits += current_number
        else:
            sum_of_odd_digits += current_number
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


string_number = input()
print(odd_and_even_sum(string_number))

# test inputs:

# 1000435

# 3495892137259234
