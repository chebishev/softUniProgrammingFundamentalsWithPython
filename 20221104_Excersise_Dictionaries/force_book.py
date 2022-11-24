force_book = {}
force_user_exists = False

while True:

    command = input()
    if command == "Lumpawaroo":
        break

    if "|" in command:

        force_side, force_user = command.split(" | ")
        force_user_exists = False

        for value in force_book.values():
            if force_user in value:
                force_user_exists = True
                break

        if not force_user_exists:
            if force_side not in force_book.keys():
                force_book[force_side] = [force_user]
            else:
                force_book[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for key, value in force_book.items():
            if force_user in value:
                force_book[key].pop(value.index(force_user))
                break
        if force_side not in force_book.keys():
            force_book[force_side] = [force_user]
        else:
            force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for key, value in force_book.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for user in value:
            print(f"! {user}")

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
