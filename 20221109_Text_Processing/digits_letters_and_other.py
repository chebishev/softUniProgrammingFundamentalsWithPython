string_to_manipulate = input()
digits, letters, others = [], [], []
for character in string_to_manipulate:
    if character.isalpha():
        letters.append(character)
    elif character.isdigit():
        digits.append(character)
    else:
        others.append(character)

print(f"{''.join(digits)}")
print(f"{''.join(letters)}")
print(f"{''.join(others)}")

# test input:

# Agd#53Dfg^&4F53
