from math import ceil

budget = float(input())
student = int(input())
flour_price = float(input())
egg_price = float(input()) * 10
apron_price = float(input())

total_eggs = student * egg_price
total_apron = ceil(student * 1.20) * apron_price
total_flour = 0

if student < 5:
    total_flour = flour_price * student
else:
    free_flour = student // 5
    total_flour = (student - free_flour) * flour_price

total_price = total_apron + total_eggs + total_flour

if total_price <= budget:
    print(f"Item purchased for the {total_price:.2f}$.")
else:
    print(f"{(total_price-budget):.2f}$ more needed.")

# test inputs:

# 50
# 2
# 1.0
# 0.10
# 10.0

# 100
# 25
# 4.0
# 1.0
# 6.0

# 946
# 20
# 12.05
# 0.42
# 27.89
