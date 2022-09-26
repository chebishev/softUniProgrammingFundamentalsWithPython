first_number = int(input())
second_number = int(input())
operation = input()
result = 0
result_type = ''

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number

if result % 2 == 0:
    result_type = "even"
else:
    result_type = 'odd'

if operation == "+" or \
        operation == "-" or \
        operation == "*":
    print(f'{first_number} {operation} {second_number} = {result} - {result_type}')
else:
    if second_number == 0:
        print(f'Cannot divide {first_number} by zero')
    else:
        if operation == '/':
            result = first_number / second_number
            print(f'{first_number} / {second_number} = {result:.2f}')
        else:
            result = first_number % second_number
            print(f'{first_number} % {second_number} = {result}')

# test input 10 12 +
# test input 10 1 -
# test input 7 3 *
# test input 123 12 /
# test input 10 3 %
# test input 112 0 /
# test input 10 0 %
