def numbers_check(lst):
    zero = 0
    negative = 0
    positive = 0
    for number in range(len(lst)):
        if lst[number] == 0:
            zero += 1
        elif lst[number] < 0:
            negative += 1
        else:
            positive += 1

    if zero > 0:
        return "zero"
    elif negative == 1 or negative == 3:
        return "negative"
    else:
        return "positive"


numbers_list = [int(input()) for number in range(3)]
print(numbers_check(numbers_list))
