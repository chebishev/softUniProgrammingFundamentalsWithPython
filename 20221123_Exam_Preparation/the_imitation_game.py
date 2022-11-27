encrypted_message = input()

while True:

    command = input()
    if command == "Decode":
        print(f"The decrypted message is: {encrypted_message}")
        break

    command = command.split("|")
    action = command[0]

    if action == "Move":
        number_of_letters = int(command[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

# test inputs:

# zzHe
# ChangeAll|z|l
# Insert|2|o
# Move|3
# Decode

# owyouh
# Move|2
# Move|3
# Insert|3|are
# Insert|9|?
# Decode
