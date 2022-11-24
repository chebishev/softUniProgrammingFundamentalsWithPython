import re

messages = int(input())
pattern = r"[star]"
attacked_planets = []
destroyed_planets = []

for message in range(messages):
    current_message = input()   # taking current input
    search_match = re.findall(pattern,current_message, re.IGNORECASE)  # matching all star ocurrences(case insensitive)
    star_list = []   # empty list for easier counting of the letters
    for character in search_match:
        star_list.append(character)   # append every starSTAR character
    decryption_key = len(star_list)   # this value will be subtracted from the ASCII of every character in the message
    new_message = ""    # decrypted message
    for character in current_message:
        new_message += chr(ord(character) - decryption_key)   # actual decrypting

    new_pattern = r"([^@\-!:>].*)?@([A-Za-z]+)([^@\-!:>].*)?:([\d]+)(.*[^@\-!:>])?!([A|D])!([^@\-!:>].*)?->([\d]+)([^@\-!:>].*)?"
    search_matches = re.split(new_pattern, new_message)
    if len(search_matches) < 10:
        continue
    else:
        planet = search_matches[2]
        population = int(search_matches[4])
        attack_type = search_matches[6]
        soldier_count = search_matches[8]
    if planet and population and attack_type and soldier_count:
        if attack_type == "A":
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)
    else:
        continue
print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")


# test inputs:

# 2
# STCDoghudd4=63333$D$0A53333
# EHfsytsnhf?8555&I&2C9555SR

# 3
# tt(''DGsvywgerx>6444444444%H%1B9444
# GQhrr|A977777(H(TTTT
# EHfsytsnhf?8555&I&2C9555SR
