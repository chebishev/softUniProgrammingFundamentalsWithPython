start = int(input())
end = int(input())
magic_number = int(input())
combinations_counter = 0
is_found = False
first_number = 0
second_number = 0

for first in range(start, end + 1):
    if is_found:
        break
    for second in range(start, end + 1):
        combinations_counter += 1
        first_number = first
        second_number = second
        if first_number + second_number == magic_number:
            is_found = True
            break
if is_found:
    print(f"Combination N:{combinations_counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combinations_counter} combinations - neither equals {magic_number}")
