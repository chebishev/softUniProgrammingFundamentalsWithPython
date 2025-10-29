initial_username = input()
command = input()

def check_index(index, string):
    if 0 > index or index >= len(string):
        return False
    return True

while command != "Registration":

    full_command = command.split()
    action = full_command[0]

    if action == "Letters":
        sub_command = full_command[1]
        if sub_command == "Lower":
            initial_username = initial_username.lower()
        else:
            initial_username = initial_username.upper()
        
        print(initial_username)

    elif action == "Reverse":
        start_index = int(full_command[1])
        end_index = int(full_command[2])
        if not check_index(start_index, initial_username) \
            or not check_index(end_index, initial_username):
            command = input()
            continue
        substring = initial_username[start_index:end_index + 1]
        print(substring[::-1])

    elif action == "Substring":
        substring = full_command[1]
        if substring in initial_username:
            # default is -1 for all occurrences
            initial_username = initial_username.replace(substring, "")
            print(initial_username)
        else:
            print(f"The username {initial_username} doesn't contain {substring}.")
    
    elif action == "Replace":
        character_to_replace = full_command[1]
        initial_username = initial_username.replace(character_to_replace, "-")
        print(initial_username)

    elif action == "IsValid":
        character_to_check = full_command[1]
        if character_to_check in initial_username:
            print("Valid username.")
        else:
            print(f"{character_to_check} must be contained in your username.")
    
    command = input()
    
# test inputs:

# John
# Letters Lower
# Substring SA
# IsValid @
# Registration

# ThisIsSoftUni
# Reverse 1 3
# Replace S
# Substring hi
# Registration
