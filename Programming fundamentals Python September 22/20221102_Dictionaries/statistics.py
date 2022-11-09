products = {}

while True:

    command = input()
    if command == "statistics":
        break

    product, quantity = command.split(": ")
    if product not in products.keys():
        products[product] = 0
    products[product] += int(quantity)

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
# [print(f"- {key}: {value}") for (product, quantity) in products]
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")

# test inputs:

# bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics

# eggs: 10
# bread: 6
# cheese: 8
# milk: 7
# statistics
