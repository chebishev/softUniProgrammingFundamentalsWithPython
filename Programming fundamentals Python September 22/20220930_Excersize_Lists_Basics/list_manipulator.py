initial_list = list(map(int, input().split()))
command = input()
while True:

    if command == "end":
        break
    operations = command.split()

    if operations[0] == "exchange":
        index = int(operations[1])
        if 0 <= index < len(initial_list):
            initial_list = initial_list[index+1:] + initial_list[:index+1]
        else:
            print("Invalid index")

    elif operations[0] == "max":
        even_odd_check = operations[1]
        max_number = -1
        max_index = 0
        if even_odd_check == "even":
            for index in range(len(initial_list)):
                current_number = initial_list[index]
                if current_number >= max_number:
                    if current_number % 2 == 0:
                        max_number = current_number
                        max_index = index
            if max_index == 0 and max_number == -1:
                print("No matches")
            print(max_index)
        else:
            for index in range(len(initial_list)):
                current_number = initial_list[index]
                if current_number >= max_number:
                    if current_number % 2 != 0:
                        max_number = current_number
                        max_index = index
            if max_index == 0 and max_number == -1:
                print("No matches")
            print(max_index)
    elif operations[0] == "min":
        even_odd_check = operations[1]
        min_number = 1001
        min_index = 0
        if even_odd_check == "even":
            for index in range(len(initial_list)):
                current_number = initial_list[index]
                if current_number <= min_number:
                    if current_number % 2 == 0:
                        min_number = current_number
                        min_index = index
            if min_index == 0 and min_number == 1001:
                print("No matches")
            else:
                print(min_index)
        else:
            for index in range(len(initial_list)):
                current_number = initial_list[index]
                if current_number <= min_number:
                    if current_number % 2 != 0:
                        min_number = current_number
                        min_index = index
            if min_index == 0 and min_number == 1001:
                print("No matches")
            else:
                print(min_index)

    elif operations[0] == "first":
        count = int(operations[1])
        even_odd_check = operations[2]
        if count > len(initial_list):
            print("Invalid count")
            command = input()
            continue
        if even_odd_check == "even":
            even_list = []
            for number in initial_list:
                if number % 2 == 0:
                    even_list.append(number)
                    if len(even_list) == count:
                        break
            print(even_list)
        else:
            odd_list = []
            for number in initial_list:
                if number % 2 != 0:
                    odd_list.append(number)
                    if len(odd_list) == count:
                        break
            print(odd_list)

    elif operations[0] == "last":
        count = int(operations[1])
        even_odd_check = operations[2]
        if count > len(initial_list):
            print("Invalid count")
            command = input()
            continue
        if even_odd_check == "even":
            even_list = []
            for index in range(len(initial_list)-1, -1, -1):
                current_number = initial_list[index]
                if current_number % 2 == 0:
                    even_list.append(current_number)
                    if count == len(even_list):
                        break
            print(even_list[::-1])
        else:
            odd_list = []
            for index in range(len(initial_list)-1, -1, -1):
                current_number = initial_list[index]
                if current_number % 2 != 0:
                    odd_list.append(current_number)
                    if count == len(odd_list):
                        break
            print(odd_list[::-1])
    command = input()

print(initial_list)
# test inputs:

# 1 3 5 7 9
# exchange 1
# max odd
# min even
# first 2 odd
# last 2 even
# exchange 3
# end

# 1 10 100 1000
# max even
# first 5 even
# exchange 10
# min odd
# exchange 0
# max even
# min even
# end

# 1 10 100 1000
# exchange 3
# first 2 odd
# last 4 odd
# end
