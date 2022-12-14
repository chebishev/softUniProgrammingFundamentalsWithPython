initial_array = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    command = command.split()
    action = command[0]

    if action == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        initial_array[first_index], initial_array[second_index] = initial_array[second_index], initial_array[first_index]

    elif action == "multiply":
        first_index = int(command[1])
        second_index = int(command[2])
        initial_array[first_index] *= initial_array[second_index]

    elif action == "decrease":
        for number in range(len(initial_array)):
            initial_array[number] -= 1

initial_array = [str(x) for x in initial_array]
print(", ".join(initial_array))

# test inputs:

# 23 -2 321 87 42 90 -123
# swap 1 3
# swap 3 6
# swap 1 0
# multiply 1 2
# multiply 2 1
# decrease
# end

# 1 2 3 4
# swap 0 1
# swap 1 2
# swap 2 3
# multiply 1 2
# decrease
# end