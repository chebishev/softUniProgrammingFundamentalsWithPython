def check_existing_side(dictionary, side):
    if side not in dictionary.keys():
        return True


force_book = {}

while True:

    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")
        if force_side not in force_book.keys() and force_user not in force_book.values():
            if check_existing_side(force_book, force_side):
                force_book[force_side] = []
            force_book[force_side].append(force_user)
        else:
            continue
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        for key, value in force_book.items():
            for index in range(len(value)):
                if force_book[key] == force_user:
                    print(key)
        print(f"{force_user} joins the {force_side} side!")

for key, value in force_book.items():
    if len(force_book[key]) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for index in range(len(value)):
            print(f"! {value[index]}")

# test inputs:

# Light | Peter
# Dark | Kim
# Light | Kim
# Lumpawaroo

# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo
