def index_is_valid(start, end):
    if 0 <= start < end:
        return True


pirate_ship_stats = list(map(int, input().split(">")))
war_ship_stats = list(map(int, input().split(">")))
max_health_capacity = int(input())
stalemate = True

while True:
    command = input().split()

    if command[0] == "Retire":
        break
    if not stalemate:
        break
    action = command[0]

    if action == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if index_is_valid(index, len(war_ship_stats)):
            war_ship_stats[index] -= damage
            if war_ship_stats[index] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    elif action == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if index_is_valid(start_index, len(pirate_ship_stats))\
                and index_is_valid(end_index, len(pirate_ship_stats)) :
            for section in range(start_index, end_index + 1):
                pirate_ship_stats[section] -= damage
                if pirate_ship_stats[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break

    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if index_is_valid(index, len(pirate_ship_stats)):
            pirate_ship_stats[index] += health
            if pirate_ship_stats[index] > max_health_capacity:
                pirate_ship_stats[index] = max_health_capacity
    elif action == "Status":
        counter = 0
        for section in range(len(pirate_ship_stats)):
            if pirate_ship_stats[section] < max_health_capacity * 0.20:
                counter += 1
        print(f"{counter} sections need repair.")

if stalemate:
    pirate_ship_sum = sum(pirate_ship_stats)
    war_ship_sum = sum(war_ship_stats)
    print(f"Pirate ship status: {pirate_ship_sum}\nWarship status: {war_ship_sum}")

# test inputs:

# 12>13>11>20>66
# 12>22>33>44>55>32>18
# 70
# Fire 2 11
# Fire 8 100
# Defend 3 6 11
# Defend 0 3 5
# Repair 1 33
# Status
# Retire

# 2>3>4>5>2
# 6>7>8>9>10>11
# 20
# Status
# Fire 2 3
# Defend 0 4 11
# Repair 3 18
# Retire
