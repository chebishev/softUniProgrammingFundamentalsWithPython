def calculations(action, first, second):
    if action == "multiply":
        return first * second
    elif action == "divide":
        return int(first / second)
    elif action == "add":
        return first + second
    elif action == "subtract":
        return first - second


command = input()
first_number = int(input())
second_number = int(input())
print(calculations(command, first_number, second_number))

# test inputs:

# subtract
# 5
# 4

# divide
# 8
# 4
