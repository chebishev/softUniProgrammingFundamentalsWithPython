import re

number_of_sequences = int(input())
pattern = r"([@][#]+)([A-Z][A-Za-z0-9]{4,}[A-Z])([@][#]+)"

for index in range(number_of_sequences):
    sequence_of_characters = input()
    search_barcode = re.findall(pattern, sequence_of_characters)
    if search_barcode:
        barcode = search_barcode[0][1]
        numbers_pattern = r"\d"
        search_numbers = re.findall(numbers_pattern, barcode)
        product_group = ""
        for number in search_numbers:
            product_group += number
        if product_group:
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")
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
