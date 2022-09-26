number_for_multiplication = float(input())

while True:
    if number_for_multiplication < 0:
        print("Negative number!")
        break
    else:
        temp = number_for_multiplication * 2
        print(f"Result: {temp:.2f}")
        number_for_multiplication = float(input())

# test input 12 43.2144 12.3 543.23 -20
# test input 23.43 12.3245 0 65.23432 23 65 -12
# test input -123
