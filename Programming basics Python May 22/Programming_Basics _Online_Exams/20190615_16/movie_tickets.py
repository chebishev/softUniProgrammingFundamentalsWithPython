first_number = int(input())
second_number = int(input())
end_range = int(input())
end_range_two = int(end_range / 2)

for symbol in range(first_number, second_number):
    for first in range(1, end_range):
        for second in range(1, end_range_two):
            if symbol % 2 != 0 and (first + second + symbol) % 2 != 0:
                print(f"{chr(symbol)}-{first}{second}{symbol}")

# test input 86 88 4
# test input 71 74 6
# test input 69 72 4
