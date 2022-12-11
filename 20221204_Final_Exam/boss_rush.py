import re

number_of_inputs = int(input())
pattern = r"\|([A-Z]{4,})\|:#([A-z]+ [A-z]+)#"

for index in range(number_of_inputs):
    current_boss = input()
    result = re.split(pattern, current_boss)
    if len(result) < 4:
        print("Access denied!")
    else:
        boss_name = result[1]
        title = result[2]
        print(f"{boss_name}, The {title}\n>> Strength: {len(boss_name)}\n>> Armor: {len(title)}")

# test inputs:

# 3
# |PETER|:#Lead architect#
# |GEORGE|:#High Overseer#
# |ALEX|:#Assistant Game Developer#

# 3
# |STEFAN|:#H1gh Overseer#
# |IVAN|:#Master detective#
# |KARL|: #Marketing lead#
