budget = float(input())
nights = int(input())
price_per_night = float(input())
others = int(input()) / 100

if nights > 7:
    price_per_night *= 0.95

total = nights * price_per_night
total += budget * others

diff = abs(budget - total)
if total > budget:
    print(f"{diff:.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")

# test input 800.50 8 100 2
# test input 500 7 66 15
