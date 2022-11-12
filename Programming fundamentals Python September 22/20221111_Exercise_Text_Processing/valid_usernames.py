words_list = input().split(", ")
# consider strip() if judge is not merciful :)
valid_symbol = False
for username in words_list:
    if 3 <= len(username) <= 16:
        for character in range(len(username)):
            valid_symbol = False
            if username[character].isalnum() or \
                    username[character] == "-" or \
                    username[character] == "_":
                valid_symbol = True
            else:
                valid_symbol = False
                break
        if valid_symbol:
            if " " not in username:
                print(username)
        else:
            continue

# test inputs:

# sh, too_long_username, !lleg@l ch@rs, jeffbutt

# Jeff, john45, ab, cd, peter-ivanov, @smith
