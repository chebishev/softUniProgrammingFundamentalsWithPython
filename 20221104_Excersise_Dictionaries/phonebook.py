phonebook = {}
command = input()

while not command.isnumeric():
    name, number = command.split("-")
    if name not in phonebook.keys():
        phonebook[name] = number
    phonebook[name] = number

    command = input()

for contact in range(int(command)):
    current_name = input()
    if current_name in phonebook.keys():
        print(f"{current_name} -> {phonebook[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")

# test inputs:

# Adam-0888080808
# 2
# Mery
# Adam

# Adam-+359888001122
# Ralf-666
# George-5559393
# Silvester-02/987665544
# 4
# Silvester
# silvester
# Rolf
# Ralf
