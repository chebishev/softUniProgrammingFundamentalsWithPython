def check_existing_side(dictionary, side):
    if side not in dictionary.keys():
        return True


force_book = {}
force_user_exists = False

while True:

    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")
        force_user_exists = False
        for value in force_book.values():
            if force_user in value:
                force_user_exists = True
                break
        if force_side not in force_book.keys() and not force_user_exists:
            force_book[force_side] = [force_user]
        elif force_side in force_book.keys() and not force_user:
            force_book[force_side].append(force_user)
        elif force_user_exists:
            continue
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        for key in force_book.keys():
            if force_user in force_book[key]:
                force_book[key].remove(force_user)
                break
        if check_existing_side(force_book, force_side):
            force_book[force_side] = []
        force_book[force_side].append(force_user)
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
