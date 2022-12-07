import re

input_count = int(input())
pattern = r"(\W*)>([\d]{3})\|([a-z]{3})\|([A-Z]{3})\|([^><]{3})<\1"
for index in range(input_count):
    current_line = input()
    current_password = re.findall(pattern, current_line)
    if current_password:
        encrypted_password = current_password[0][1] + current_password[0][2] + current_password[0][3] + current_password[0][4]
        print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")

# test inputs:

# 3
# ##>00|no|NO|!!!?<###
# ##>123|yes|YES|!!!<##
# $$<111|noo|NOPE|<<>$$

# 5
# aa>111|mqu|BAU|mqu<aa
# ()>111!aaa!AAA!^&*<()
# o>088|abc|AAA|***<o
# asd>asd|asd|ASD|asd<asd
# *>088|zzzz|ZzZ|123<*
