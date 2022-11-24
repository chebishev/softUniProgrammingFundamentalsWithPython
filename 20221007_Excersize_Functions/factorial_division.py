def factorial_division(num1, num2):
    for numbers in range(1, num1):
        num1 *= numbers
    for numbers in range(1, num2):
        num2 *= numbers
    return f"{(num1 / num2):.2f}"


factorial = int(input())
divisor = int(input())
print(factorial_division(factorial, divisor))

# test inputs:

# 5
# 2

# 6
# 2
