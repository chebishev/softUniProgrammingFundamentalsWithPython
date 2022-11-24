import re

line = input()
customer_pattern = r"%([A-Z][a-z]+)%"
product_pattern = r"<([\w]+)>"
count_pattern = r"\|([\d]+)\|"
price_pattern = r"([\d]+(\.[\d]+)*)\$"
total = 0
while line != "end of shift":
    customer = re.findall(customer_pattern, line)
    product = re.findall(product_pattern, line)
    count = re.findall(count_pattern, line)
    price = re.findall(price_pattern, line)
    if customer and product and count and price:
        price = float(price[0][0])
        count = int(count[0])
        print(f"{customer[0]}: {product[0]} - {(price * count):.2f}")
        total += price * count
    line = input()
print(f"Total income: {total:.2f}")

# test inputs:

# %George%<Croissant>|2|10.3$
# %Peter%<Gum>|1|1.3$
# %Maria%<Cola>|1|2.4$
# end of shift

# %InvalidName%<Croissant>|2|10.3$
# %Peter%<Gum>1.3$
# %Maria%<Cola>|1|2.4
# %Valid%<Valid>valid|10|valid20$
# end of shift
