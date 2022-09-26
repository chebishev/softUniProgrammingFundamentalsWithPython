microbus_tones = 0
truck_tones = 0
train_tones = 0
total_tones = 0
price = 0

for numbers in range(int(input())):
    cargo_tones = int(input())
    total_tones += cargo_tones

    if cargo_tones <= 3:
        price += cargo_tones * 200
        microbus_tones += cargo_tones
    elif cargo_tones < 12:
        price += cargo_tones * 175
        truck_tones += cargo_tones
    else:
        price += cargo_tones * 120
        train_tones += cargo_tones

average_price = price / total_tones

microbus_percent = microbus_tones / total_tones * 100
truck_percent = truck_tones / total_tones * 100
train_percent = train_tones / total_tones * 100

print(f'{average_price:.2f}')
print(f'{microbus_percent:.2f}%')
print(f'{truck_percent:.2f}%')
print(f'{train_percent:.2f}%')

# test input 4 1 5 16 3
# test input 5 2 10 20 1 7
