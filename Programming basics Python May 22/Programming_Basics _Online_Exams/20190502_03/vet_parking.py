days = int(input())
hours_per_day = int(input())
total = 0
for day in range(1, days+1):
    price = 0
    for hour in range(1, hours_per_day+1):
        if day % 2 != 0:
            if hour % 2 == 0:
                price += 1.25
            else:
                price += 1
        else:
            if hour % 2 != 0:
                price += 2.50
            else:
                price += 1
    print(f"Day: {day} - {price:.2f} leva")
    total += price
print(f"Total: {total:.2f} leva")

# test input 2 5
# test input 5 2
