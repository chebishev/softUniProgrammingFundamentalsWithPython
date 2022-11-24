number = int(input())
counter = 0
is_prime = False
for i in range(2, number+1):
    if number % i == 0:
        counter += 1

if counter == 1:
    is_prime = True

print(is_prime)

# test inputs:

# 7

# 8

# 81
