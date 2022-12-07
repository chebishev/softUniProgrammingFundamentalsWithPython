players_pool = {}

while True:

    command = input()
    if command == "Season end":
        break

    if " vs " in command:
        player_one, player_two = command.split(" vs ")
        if player_one in players_pool.keys() and player_two in players_pool.keys():
            for position in players_pool[player_one].keys():
                if position in players_pool[player_two].keys():
                    if sum(players_pool[player_one].values()) > sum(players_pool[player_two].values()):
                        del players_pool[player_two]
                        break
                    elif sum(players_pool[player_one].values()) < sum(players_pool[player_two].values()):
                        del players_pool[player_one]
                        break
                    else:
                        continue

    elif " -> " in command:
        command = command.split(" -> ")
        player, position, skill = command[0], command[1], int(command[2])
        if player not in players_pool.keys():
            players_pool[player] = {position: skill}
        else:
            if position in players_pool[player].keys():
                if players_pool[player][position] < skill:
                    players_pool[player][position] = skill
            else:
                players_pool[player][position] = skill

total_dict = {"total": {}}
for key, value in players_pool.items():
    total = 0
    for position, skill in value.items():
        total += skill
    total_dict["total"][key] = total

for key, value in total_dict.items():
    for name, total in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f"{name}: {total} skill")
        for position, skills in sorted(players_pool[name].items(), key=lambda x: (-x[1], x[0])):
            print(f"- {position} <::> {skills}")

# 80/100

# test inputs:

# Peter -> Adc -> 400
# George -> Jungle -> 300
# Simon -> Mid -> 200
# Simon -> Support -> 250
# Season end

# Peter -> Adc -> 400
# Bush -> Tank -> 150
# Frank -> Mid -> 200
# Frank -> Support -> 250
# Frank -> Tank -> 250
# Peter vs Frank
# Frank vs Bush
# Frank vs Hide
# Season end
