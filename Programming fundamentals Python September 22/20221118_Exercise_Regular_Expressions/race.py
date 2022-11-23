import re

valid_racers = input().split(", ")
race = {}
string = input()
letters = r"[A-Za-z]"
numbers = r"[\d]"
driver = ""
distance = 0
while string != "end of race":

    name = re.findall(letters, string)
    for letter in name:
        driver += letter
    if driver in valid_racers:
        if driver not in race.keys():
            race[driver] = 0
    else:
        driver = ""
        string = input()
        continue

    mileage = re.findall(numbers, string)
    for number in mileage:
        distance += int(number)
    race[driver] += distance
    driver = ""
    distance = 0
    string = input()

final_list = sorted(race.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {final_list[0][0]}")
print(f"2nd place: {final_list[1][0]}")
print(f"3rd place: {final_list[2][0]}")

# test input:

# George, Peter, Bill, Tom
# G4e@55or%6g6!68e!!@
# R1@!3a$y4456@
# B5@i@#123ll
# G@e54o$r6ge#
# 7P%et^#e5346r
# T$o553m&6
# end of race
