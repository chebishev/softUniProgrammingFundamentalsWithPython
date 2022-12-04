import re

check_eggs = input()
pattern = r"[@|#]+([a-z]{3,})[@|#]+?(\.*[^A-Za-z0-9]*)([\/]+)([\d]+)([\/]+)"
search_pattern = re.findall(pattern, check_eggs)
for match in search_pattern:
    color = match[0]
    amount = int(match[3])
    if color and amount:
        print(f"You found {amount} {color} eggs!")

# test inputs:

# @@@@green@*/10/@yel0w@*26*#red#####//8//@limon*@*23*@@@red#*/%^&/6/@gree_een@/notnumber/###purple@@@@@*$%^&*/5/

# #@##@red@#/8/@rEd@/2/#@purple@////10/

# https://softwareuniversity-my.sharepoint.com/:w:/g/personal/joana_veskova_students_softuni_bg/EZyfvL9dYUBImdmv0duUxfsBLycFfCqWlczTwpp5szI79w?e=XP9IOI
