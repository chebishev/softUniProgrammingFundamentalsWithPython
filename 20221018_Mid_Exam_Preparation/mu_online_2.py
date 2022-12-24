health = 100
bitcoin = 0
room_counter = 0
is_dead = False
rooms = input().split("|")
for room in rooms:
    current_room = room.split()
    room_counter += 1
    item_found = current_room[0]
    value = int(current_room[1])
    if item_found == "potion":
        current_heal = 0
        if health + value > 100:
            current_heal = 100 - health
            health = 100
        else:
            health += value
            current_heal = value
        print(f"You healed for {current_heal} hp.")
        print(f"Current health: {health} hp.")

    elif item_found == "chest":
        bitcoin += value
        print(f'You found {value} bitcoins.')
    else:
        if health - value <= 0:
            is_dead = True
            break
        else:
            health -= value
            print(f"You slayed {item_found}.")

if is_dead:
    print(f"You died! Killed by {item_found}.")
    print(f"Best room: {room_counter}")
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")

# test inputs:

# rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000

# cat 10|potion 30|orc 10|chest 10|snake 25|chest 110
