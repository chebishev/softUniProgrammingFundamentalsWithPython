encrypted_message = input()

while True:
    command = input()
    if command == "Decode":
        print(f"The decrypted message is: {encrypted_message}")
        break

    command_list = command.split("|")
    action = command_list[0]
    
    if action == "Move":
        number_of_letters_to_move = int(command_list[1])
        first_part = encrypted_message[:number_of_letters_to_move]
        second_part = encrypted_message[number_of_letters_to_move:]
        encrypted_message = second_part + first_part
    
    elif action == "Insert":
        index = int(command_list[1])
        value = command_list[2]
        new_encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
        encrypted_message = new_encrypted_message

    elif action == "ChangeAll":
        substring = command_list[1]
        replacement = command_list[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

# test inputs:

# zzHe
# ChangeAll|z|l
# Insert|2|o
# Move|3

# owyouh
# Move|2
# Move|3
# Insert|3|are
# Insert|9|?
# Decode

