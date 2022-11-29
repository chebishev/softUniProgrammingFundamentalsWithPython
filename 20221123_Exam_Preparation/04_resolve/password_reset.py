password = input()

while True:

    command = input()
    if command == "Done":
        print(f"Your password is: {password}")
        break

    command = command.split()
    action = command[0]

    if action == "TakeOdd":
        new_password = ""
        for index in range(len(password)):
            if index % 2 != 0:
                new_password += password[index]
        password = new_password
        print(password)

    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        substring = password[index:index+length]
        password = password.replace(substring, "", 1)
        print(password)

    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

# test inputs:

# Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr
# TakeOdd
# Cut 15 3
# Substitute :: -
# Substitute | ^
# Done

# Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr
# TakeOdd
# Cut 15 3
# Substitute :: -
# Substitute | ^
# Done