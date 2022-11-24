def orders(string, count):
    if string == "coffee":
        result = count * 1.50
    elif string == "coke":
        result = count * 1.40
    elif string == "water":
        result = count * 1.00
    elif string == "snacks":
        result = count * 2.00
    return f"{result:.2f}"


product = input()
quantity = int(input())
print(orders(product, quantity))

# test inputs:

# water
# 5

# coffee
# 2
