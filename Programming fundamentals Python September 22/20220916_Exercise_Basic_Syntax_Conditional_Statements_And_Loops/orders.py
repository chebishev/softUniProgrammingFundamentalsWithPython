orders_count = int(input())
total_price = 0

for order in range(orders_count):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not 0.01 <= capsule_price <= 100.00 or \
            not 1 <= days <= 31 or \
            not 1 <= capsules_per_day <= 2000:
        continue
    price = capsule_price * days * capsules_per_day
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price

print(f"Total: ${total_price:.2f}")

# test inputs:

# 1
# 1.53
# 30
# 8

# 2
# 4.99
# 31
# 3
# 0.35
# 31
# 5

# 2
# 9.223
# 31
# 0
# 0.05
# 10
# 30
