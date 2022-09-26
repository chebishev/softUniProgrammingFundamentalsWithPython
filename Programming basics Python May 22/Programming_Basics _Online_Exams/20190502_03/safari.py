budget = float(input())
needed_litters = float(input())
day_of_week = input()

guide_price = 100
litter_price = 2.10

total = needed_litters * litter_price + guide_price
if day_of_week == "Saturday":
    total *= 0.90
else:
    total *= 0.80
diff = abs(budget - total)
if budget >= total:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")

# test input 1000 10 Sunday
# test input 120 30 Saturday
# test input 105.20 15 Sunday
