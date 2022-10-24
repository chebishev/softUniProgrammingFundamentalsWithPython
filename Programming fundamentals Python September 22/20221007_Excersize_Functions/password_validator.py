def password_validator(passphrase):
    list_print = []
    length = False
    alpha_num = False
    two_digits = False
    digit_counter = 0
    for character in passphrase:
        if character.isdigit():
            digit_counter += 1

    if passphrase.isalnum():
        alpha_num = True
    if digit_counter < 2:
        pass
    else:
        two_digits = True
    if 6 <= len(passphrase) <= 10:
        length = True

    if alpha_num and two_digits and length:
        list_print.append("Password is valid")
    else:
        if not length:
            list_print.append("Password must be between 6 and 10 characters")
        if not alpha_num:
            list_print.append("Password must consist only of letters and digits")
        if not two_digits:
            list_print.append("Password must have at least 2 digits")
    return list_print


password = input()
print(*password_validator(password), sep="\n")

# test inputs:

# logIn

# MyPass123

# Pa$s$s
