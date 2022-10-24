initial_health = 100
initial_bitcoins = 0
succeed = True

rooms = input().split("|")
for index in range(len(rooms)):
    room = rooms[index].split()
    command = room[0]
    value = int(room[1])

    if command == "potion":
        current_amount = 0
        if initial_health + value > 100:
            current_amount = 100 - initial_health
            initial_health = 100
        else:
            current_amount = value
            initial_health += value
        print(f"You healed for {current_amount} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        initial_bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        initial_health -= value
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {index+1}")
            succeed = False
            break

if succeed:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")

# test inputs:

# rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000

# cat 10|potion 30|orc 10|chest 10|snake 25|chest 110
