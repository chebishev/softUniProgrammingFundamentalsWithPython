start_letter = ord(input())
end_letter = ord(input())
not_printed_letter = ord(input())
counter = 0

for first_letter in range(start_letter, end_letter + 1):
    for second_letter in range(start_letter, end_letter + 1):
        for third_letter in range(start_letter, end_letter + 1):
            if first_letter == not_printed_letter or \
                    second_letter == not_printed_letter or \
                    third_letter == not_printed_letter:
                continue
            else:
                print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}", end=" ")
                counter += 1
print(counter)

# test input a c b
# test input f k h
# test input a c z
