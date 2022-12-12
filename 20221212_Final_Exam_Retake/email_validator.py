email = input()

while True:

    command = input()
    if command == "Complete":
        break

    if command == "Make Upper":
        email = email.upper()
        print(email)

    elif command == "Make Lower":
        email = email.lower()
        print(email)

    elif command.startswith("GetDomain "):
        command = command.split()
        count = int(command[1])
        start_index = len(email) - count
        print(email[start_index:len(email)])

    elif command == "GetUsername":
        if "@" not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            substring = ""
            for character in email:
                if character == "@":
                    break
                else:
                    substring += character
            print(substring)

    elif command.startswith("Replace "):
        command = command.split()
        char = command[1]
        email = email.replace(char, "-")
        print(email)

    elif command == "Encrypt":
        for symbol in email:
            print(ord(symbol), end=" ")

# test inputs:

# Mike123@somemail.com
# Make Upper
# GetDomain 3
# GetUsername
# Encrypt
# Complete

# AnotherMail.com
# Make Lower
# GetUsername
# Replace a
# Complete

# Another@Mail.com
# Make Lower
# GetUsername
# GetDomain 3
# Encrypt
# Complete