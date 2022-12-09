initial_energy = int(input())
count = 0
battle_count = 0
while True:

    command = input()
    if command == "End of battle":
        print(f"Won battles: {count}. Energy left: {initial_energy}")
        break

    distance = int(command)
    battle_count += 1

    if initial_energy >= distance:
        initial_energy -= distance
        count += 1
    else:
        print(f"Not enough energy! Game ends with {count} won battles and {initial_energy} energy")
        break

    if battle_count % 3 == 0:
        initial_energy += count

# test inputs:

# 100
# 10
# 10
# 10
# 1
# 2
# 3
# 73
# 10

# 200
# 54
# 14
# 28
# 13
# End of battle
