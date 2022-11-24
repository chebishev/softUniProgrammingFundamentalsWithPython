miner_dictionary = {}

while True:

    command = input()

    if command == "stop":
        break

    resource = command
    quantity = int(input())

    if resource not in miner_dictionary.keys():
        miner_dictionary[resource] = 0
    miner_dictionary[resource] += quantity

for key, value in miner_dictionary.items():
    print(f"{key} -> {value}")

# test inputs:

# Gold
# 155
# Silver
# 10
# Copper
# 17
# stop

# gold
# 155
# silver
# 10
# copper
# 17
# gold
# 15
# stop
