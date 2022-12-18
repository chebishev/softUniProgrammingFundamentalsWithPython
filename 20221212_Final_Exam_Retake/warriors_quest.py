skill_to_decipher = input()

while True:

    command = input()
    if command == "For Azeroth":
        break

    elif command == "GladiatorStance":
        skill_to_decipher = skill_to_decipher.upper()
        print(skill_to_decipher)

    elif command == "DefensiveStance":
        skill_to_decipher = skill_to_decipher.lower()
        print(skill_to_decipher)

    else:
        command = command.split()
        action = command[0]
        if action == "Dispel":
            index = int(command[1])
            letter = command[2]
            if 0 <= index < len(skill_to_decipher):
                letter_to_change = skill_to_decipher[index]
                skill_to_decipher = skill_to_decipher[:index] + letter + skill_to_decipher[index + 1:]
                print("Success")
            else:
                print("Dispel too weak.")
        elif action == "Target":
            operation = command[1]
            if operation == "Change":
                first_substring = command[2]
                second_substring = command[3]
                if first_substring in skill_to_decipher:
                    skill_to_decipher = skill_to_decipher.replace(first_substring, second_substring)
                    print(skill_to_decipher)
                else:
                    print(skill_to_decipher)

            elif operation == "Remove":
                substring = command[2]
                if substring in skill_to_decipher:
                    skill_to_decipher = skill_to_decipher.replace(substring, "", 1)
                    print(skill_to_decipher)
            else:
                print("Command doesn't exist!")
        else:
            print("Command doesn't exist!")

# test inputs:

# fr1c710n
# GladiatorStance
# Dispel 2 I
# Dispel 4 T
# Target Change RICTION riction
# For Azeroth

# DYN4MICNIC
# Target Remove NIC
# Dispel 3 A
# DefensiveStance
# Target Change d D
# target change D d
# For Azeroth
