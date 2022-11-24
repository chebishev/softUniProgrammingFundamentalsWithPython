def perfect_number(num):
    sum_of_numbers = 0
    for n in range(1, num // 2 + 1):
        if num % n == 0:
            sum_of_numbers += n
    if sum_of_numbers == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))

# test inputs:

# 6

# 28

# 1236498
