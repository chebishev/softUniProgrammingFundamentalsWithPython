painting_accession_numbers = [int(x) for x in input().split()]

while True:

    command = input()
    if command == "END":
        break

    command = command.split()
    action = command[0]

    if action == "Change":
        painting_number = int(command[1])
        new_number = int(command[2])
        if painting_number in painting_accession_numbers:
            painting_accession_numbers[painting_accession_numbers.index(painting_number)] = new_number

    elif action == "Hide":
        painting_number = int(command[1])
        if painting_number in painting_accession_numbers:
            painting_accession_numbers.remove(painting_number)

    elif action == "Switch":
        first_number = int(command[1])
        second_number = int(command[2])
        if first_number in painting_accession_numbers and second_number in painting_accession_numbers:
            first_index = painting_accession_numbers.index(first_number)
            second_index = painting_accession_numbers.index(second_number)
            painting_accession_numbers[first_index], painting_accession_numbers[second_index] = painting_accession_numbers[second_index], painting_accession_numbers[first_index]

    elif action == "Insert":
        index = int(command[1]) + 1
        painting_number = int(command[2])
        if 0 <= index < len(painting_accession_numbers):
            painting_accession_numbers.insert(index, painting_number)

    elif action == "Reverse":
        painting_accession_numbers = painting_accession_numbers[::-1]

print(*painting_accession_numbers, end=" ")

# test inputs:

# 115 101 114 73 111 116 75
# Insert 5 144
# Switch 116 73
# Hide 76
# END

# 77 120 115 101 97 78 88 112 111 108 110
# Switch 97 98
# Hide 88
# Change 120 117
# END

# 65 304 97 79 12 659
# Reverse
# Change 73 70
# Insert 10 85
# END
