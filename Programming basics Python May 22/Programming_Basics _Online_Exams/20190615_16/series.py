budget = float(input())
tv_series_count = int(input())
total = 0
for tv_series in range(tv_series_count):
    tv_series_name = input()
    price = float(input())
    if tv_series_name == "Thrones":
        price *= 0.50
    elif tv_series_name == "Lucifer":
        price *= 0.60
    elif tv_series_name == "Protector":
        price *= 0.70
    elif tv_series_name == "TotalDrama":
        price *= 0.80
    elif tv_series_name == "Area":
        price *= 0.90
    total += price

diff = abs(total - budget)
if total > budget:
    print(f"You need {diff:.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {diff:.2f} lv.")

# test input 10 3 Thrones 5 Riverdale 5 Gotham 2
# test input 25 6 Teen Wolf 8 Protector 5 TotalDrama 5 Area 4 Thrones 5 Lucifer 9
