import re

number_of_messages = int(input())
key_pattern = r"[STARstar]"
star_enigma_dict = {"Attacked planets:": [], "Destroyed planets:": []}
for message in range(number_of_messages):
    current_message = input()
    key_search = re.findall(key_pattern, current_message)
    key = len(key_search)
    secret_message = ""
    for char in range(len(current_message)):
        secret_message += chr(ord(current_message[char]) - key)
    planet_pattern = r"([^@\-:>!])*(@([A-Za-z]+))([^@\-:>!])*(:([\d]+))([^@\-:>!])*(!([A|D])!)([^@\-:>!])*(->([\d]+))"
    planet_search = re.findall(planet_pattern, secret_message)
    if planet_search:
        planet = planet_search[0][2]
        population = int(planet_search[0][5])
        attack_type = planet_search[0][8]
        soldier_count = int(planet_search[0][11])
        if attack_type == "A":
            star_enigma_dict["Attacked planets:"].append(planet)
        elif attack_type == "D":
            star_enigma_dict["Destroyed planets:"].append(planet)

for key in sorted(star_enigma_dict.keys()):
    print(f"{key} {len(star_enigma_dict[key])}")
    for planet in sorted(star_enigma_dict[key]):
        print(f"-> {planet}")

# test inputs:

# 2
# STCDoghudd4=63333$D$0A53333
# EHfsytsnhf?8555&I&2C9555SR

# 3
# tt(''DGsvywgerx>6444444444%H%1B9444
# GQhrr|A977777(H(TTTT
# EHfsytsnhf?8555&I&2C9555SR
