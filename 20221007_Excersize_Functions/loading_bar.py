def loading_bar(num):
    if num == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        current_num = num // 10
        percents = current_num * "%"
        dots = (10 - current_num) * "."
        return f"{num}% [{percents}{dots}]\nStill loading..."


number = int(input())
print(loading_bar(number))

# Test inputs:

# 30

# 50

# 100
