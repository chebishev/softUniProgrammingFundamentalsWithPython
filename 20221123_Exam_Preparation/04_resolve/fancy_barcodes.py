import re

barcodes_count = int(input())
pattern = r"[@][#]+([A-Z][A-Za-z\d]{4,}[A-Z])[@][#]+"

for line in range(barcodes_count):
    barcode = input()
    search_barcode = re.findall(pattern, barcode)
    if search_barcode:
        product_group = ""
        for number in search_barcode[0]:
            if number.isdigit():
                product_group += number
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")

# test inputs:

# 3
# @#FreshFisH@#
# @###Brea0D@###
# @##Che4s6E@##

# 6
# @###Val1d1teM@###
# @#ValidIteM@#
# ##InvaliDiteM##
# @InvalidIteM@
# @#Invalid_IteM@#
# @#ValiditeM@#
