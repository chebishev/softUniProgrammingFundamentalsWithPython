hundreds_range = int(input())
tens_range = int(input())
ones_range = int(input())

for hundreds in range(1, hundreds_range + 1):
    for tens in range(2, tens_range + 1):
        for ones in range(1, ones_range + 1):
            if hundreds % 2 == 0 and ones % 2 == 0:
                if tens == 2 or \
                        tens == 3 or \
                        tens == 5 or \
                        tens == 7:
                    print(f"{hundreds} {tens} {ones}")
                else:
                    continue

# test input 3 5 5
# test input 8 2 8
