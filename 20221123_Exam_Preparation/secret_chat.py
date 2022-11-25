secret_message = input()

while True:

    command = input()

    if command == "Reveal":
        print(f"You have a new text message: {secret_message}")
        break

    command = command.split(":|:")
    action = command[0]

    if action == "InsertSpace":
        index = int(command[1])
        secret_message = secret_message[:index] + " " + secret_message[index:]
        print(secret_message)

    elif action == "Reverse":
        substring = command[1]
        if substring in secret_message:
            secret_message = secret_message.replace(substring, "", 1)
            secret_message += substring[::-1]
            print(secret_message)
        else:
            print("error")

    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in secret_message:
            secret_message = secret_message.replace(substring, replacement)
        print(secret_message)

# test inputs:

# heVVodar!gniV
# ChangeAll:|:V:|:l
# Reverse:|:!gnil
# InsertSpace:|:5
# Reveal

# Hiware?uiy
# ChangeAll:|:i:|:o
# Reverse:|:?uoy
# Reverse:|:jd
# InsertSpace:|:3
# InsertSpace:|:7
# Reveal
