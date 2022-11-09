products = input().split()
stock = {}
check_list = input().split()

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index + 1])
    stock[key] = value

for product in check_list:
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

# test inputs:

# cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes

# eggs 5 bread 10
# bread eggs
