import re

furniture = []
command = input()
pattern = r'[>]{2}([A-Z][A-Za-z]+)[<]{2}([\d]+[\.]*[\d]+)\!([\d]+)'
total = 0
while command != "Purchase":

    current_item = re.findall(pattern, command)
    if current_item:
        furniture.append(current_item[0][0])
        price = float(current_item[0][1])
        quantity = int(current_item[0][2])
        total += price * quantity
        command = input()
    else:
        command = input()
        continue

print("Bought furniture:")
if furniture:
    for item in furniture:
        print(item)
print(f"Total money spend: {total:.2f}")

# test input:

# >>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase
