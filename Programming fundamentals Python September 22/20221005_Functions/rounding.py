def rounding_function(list):
    rounded_numbers = []
    for item in list:
        current_number = round(float(item))
        rounded_numbers.append(current_number)
    return rounded_numbers


floated_numbers_list = input().split()
print(rounding_function(floated_numbers_list))
