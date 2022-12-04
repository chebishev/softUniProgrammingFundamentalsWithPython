string_decrypt = input()

while True:

    command = input()
    if command == "Finish":
        break

    command = command.split()
    action = command[0]

    if action == "Replace":
        current_char = command[1]
        new_char = command[2]
        string_decrypt = string_decrypt.replace(current_char, new_char)
        print(string_decrypt)

    elif action == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(string_decrypt) and start_index <= end_index < len(string_decrypt):
            string_to_cut = string_decrypt[start_index:end_index+1]
            string_decrypt = string_decrypt.replace(string_to_cut, "", 1)
            print(string_decrypt)
        else:
            print("Invalid indices!")

    elif action == "Make":
        transform = command[1]
        if transform == "Upper":
            string_decrypt = string_decrypt.upper()
        else:
            string_decrypt = string_decrypt.lower()
        print(string_decrypt)

    elif action == "Check":
        string = command[1]
        if string in string_decrypt:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif action == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(string_decrypt) and start_index <= end_index < len(string_decrypt):
            substring = string_decrypt[start_index:end_index+1]
            sum_ascii = 0
            for char in substring:
                sum_ascii += ord(char)
            print(sum_ascii)
        else:
            print("Invalid indices!")

# test inputs:

# ILikeSoftUni
# Replace I We
# Make Upper
# Check SoftUni
# Sum 1 4
# Cut 1 4
# Finish

# HappyNameDay
# Replace p r
# Make Lower
# Cut 2 23
# Sum -2 2
# Finish
