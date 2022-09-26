juniors = int(input())
seniors = int(input())
trace_type = input()
tax = 0

if trace_type == "trail":
    tax = juniors * 5.50 + seniors * 7
elif trace_type == "cross-country":
    tax = juniors * 8 + seniors * 9.50
    if juniors + seniors >= 50:
        tax *= 0.75
elif trace_type == "downhill":
    tax = juniors * 12.25 + seniors * 13.75
else:
    tax = juniors * 20 + seniors * 21.50

donations = tax * 0.95

print(f'{donations:.2f}')

# test input 10 20 trail
# test input 21 26 cross-country
# test input 30 25 cross-country
# test input 10 10 downhill
# test input 3 40 road
