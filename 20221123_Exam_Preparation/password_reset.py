password = input()
while True:

    command = input()
    if command == "Done":
        print(f"Your password is: {password}")
        break

    command = command.split()
    action = command[0]

    if action == "TakeOdd":
        raw_password = ""
        for index in range(len(password)):
            if index % 2 != 0:
                raw_password += password[index]
        password = raw_password
        print(password)

    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        string_to_cut = password[index:(index+length)]
        password = password.replace(string_to_cut, "", 1)
        print(password)

    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

# test input:

# Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr
# TakeOdd
# Cut 15 3
# Substitute :: -
# Substitute | ^
# Done
