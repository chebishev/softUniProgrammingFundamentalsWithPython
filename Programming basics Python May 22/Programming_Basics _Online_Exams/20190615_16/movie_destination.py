movie_budget = float(input())
destination = input()
season = input()
days = int(input())
price_per_day = 0

if season == "Winter":
    if destination == "Dubai":
        price_per_day = 45000
    elif destination == "Sofia":
        price_per_day = 17000
    else:
        price_per_day = 24000
else:
    if destination == "Dubai":
        price_per_day = 40000
    elif destination == "Sofia":
        price_per_day = 12500
    else:
        price_per_day = 20250

total = days * price_per_day
if destination == "Dubai":
    total *= 0.70
if destination == "Sofia":
    total *= 1.25
diff = abs(total - movie_budget)
if total <= movie_budget:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")

# test input 400000 Sofia Winter 20
# test input 1000000 Dubai Summer 5
# test input 200000 London Summer 7
