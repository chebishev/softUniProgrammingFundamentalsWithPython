destination = input()
package = input()
vip = input()
days = int(input())
price_per_day = 0
is_invalid = False
if destination == "Bansko" or \
        destination == "Borovets":
    if package == "withEquipment":
        price_per_day = 100
        if vip == "yes":
            price_per_day *= 0.90
    elif package == "noEquipment":
        price_per_day = 80
        if vip == "yes":
            price_per_day *= 0.95
    else:
        is_invalid = True
elif destination == "Varna" or \
        destination == "Burgas":
    if package == "withBreakfast":
        price_per_day = 130
        if vip == "yes":
            price_per_day *= 0.88
    elif package == "noBreakfast":
        price_per_day = 100
        if vip == "yes":
            price_per_day *= 0.93
    else:
        is_invalid = True
else:
    is_invalid = True
if days > 7:
    days -= 1
total = days * price_per_day
if days < 1 or is_invalid:
    if days < 1:
        print("Days must be positive number!")
    if is_invalid:
        print("Invalid input!")
else:
    print(f"The price is {total:.2f}lv! Have a nice time!")

# test inputs

# Borovets
# noEquipment
# yes
# 6

# Bansko
# withEquipment
# no
# 2

# Varna
# withBreakfast
# yes
# 5

# Burgas
# noBreakfast
# no
# 4

# Varna
# withBreakfast
# no
# 0

# Gabrovo
# noBreakfast
# no
# 3
