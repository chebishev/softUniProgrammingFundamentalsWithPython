products = input().split()
bakery = {}

for index in range(0, len(products), 2):
    bakery[products[index]] = int(products[index + 1])

print(bakery)


# test inputs:

# bread 10 butter 4 sugar 9 jam 12

# eggs 3 sugar 7 salt 1 butter 3
