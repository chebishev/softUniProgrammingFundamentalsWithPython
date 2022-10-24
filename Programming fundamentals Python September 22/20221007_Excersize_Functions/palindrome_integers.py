def palindrome_test(numbers):
    palindrome_list = []
    for number in numbers:
        if number == number[::-1]:
            palindrome_list.append("True")
        else:
            palindrome_list.append("False")
    return palindrome_list


integers = input().split(", ")
print(*palindrome_test(integers), sep="\n")

# test inputs:

# 123, 323, 421, 121

# 32, 2, 232, 1010
