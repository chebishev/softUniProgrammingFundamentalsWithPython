kilometers = int(input())
time_of_day = input()
total = 0

if kilometers < 20:
    if time_of_day == "day":
        total = (kilometers * 0.79) + 0.70
    else:
        total = (kilometers * 0.90) + 0.70
elif kilometers < 100:
    total = kilometers * 0.09
else:
    total = kilometers * 0.06

print(f'{total:.2f}')

# test input 5 day
# test input 7 night
# test input 25 day
# test input 180 night
