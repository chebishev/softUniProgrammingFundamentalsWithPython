start = int(input())
end = int(input())

for first_number in range(start, end+1):
    for second_number in range(start, end + 1):
        for third_number in range(start, end + 1):
            for fourth_number in range(start, end + 1):
                if first_number <= fourth_number:
                    continue
                if (first_number % 2 == 0 and fourth_number % 2 == 0) or \
                        (first_number % 2 != 0 and fourth_number % 2 != 0):
                    continue
                if (second_number + third_number) % 2 == 0:
                    print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")
                else:
                    continue
