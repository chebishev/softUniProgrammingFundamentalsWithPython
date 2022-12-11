spell_to_decipher = input()

while True:

    command = input()
    if command == "Abracadabra":
        break

    command = command.split()
    spell = command[0]

    if spell == "Abjuration":
        spell_to_decipher = spell_to_decipher.upper()
        print(spell_to_decipher)

    elif spell == "Necromancy":
        spell_to_decipher = spell_to_decipher.lower()
        print(spell_to_decipher)

    elif spell == "Illusion":
        index = int(command[1])
        letter = command[2]
        if 0 <= index < len(spell_to_decipher):
            spell_to_decipher = spell_to_decipher[:index] + letter + spell_to_decipher[index+1:]
            print("Done!")
        else:
            print("The spell was to weak.")

    elif spell == "Divination":
        first_substring = command[1]
        second_substring = command[2]
        if first_substring in spell_to_decipher:
            spell_to_decipher = spell_to_decipher.replace(first_substring, second_substring)

    elif spell == "Alteration":
        substring = command[1]
        if substring in spell_to_decipher:
            spell_to_decipher = spell_to_decipher.replace(substring, "")
            print(spell_to_decipher)

    else:
        print("The spell did not work!")


# test inputs:

# A7ci0
# Illusion 1 c
# Illusion 4 o
# Abjuration
# Abracadabra

# TR1GG3R
# Necromancy
# Illusion 8 m
# Illusion 9 n
# Abracadabra

# Swordmaster
# Target Target Target
# Abjuration
# Necromancy
# Alteration master
# Abracadabra