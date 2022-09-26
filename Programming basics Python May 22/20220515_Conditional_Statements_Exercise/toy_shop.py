trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzles_total = puzzles_count * 2.60
dolls_total = dolls_count * 3
bears_total = bears_count * 4.10
minions_total = minions_count * 8.20
truck_total = trucks_count * 2

total_sum = puzzles_total + dolls_total + bears_total + minions_total + truck_total

if (puzzles_count + dolls_count + bears_count + minions_count + trucks_count) >= 50:
    total_sum *= 0.75

total_sum = total_sum - (total_sum * 0.10)

if trip_price <= total_sum:
    print(f'Yes! {(total_sum - trip_price):.2f} lv left.')
else:
    print(f'Not enough money! {(trip_price - total_sum):.2f} lv needed.')

# test input 40.8 20 25 30 50 10
# test input 320 8 2 5 5 1
