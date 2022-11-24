working_day_events = input().split("|")
energy = 100
coins = 100
day_completed = True

for item in working_day_events:
    current_item = item.split("-")
    command = current_item[0]
    value = int(current_item[1])
    if command == "rest":
        if energy == 100:
            value = 0
        elif energy < 100:
            current_energy = energy + value
            if current_energy > 100:
                value = 100 - energy
                energy = 100
            else:
                energy = current_energy
        print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")
    elif command == "order":
        if energy < 30:
            energy += 50
            print("You had to rest!")
            continue
        energy -= 30
        coins += value
        print(f"You earned {value} coins.")
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {command}.")
        else:
            day_completed = False
            print(f"Closed! Cannot afford {command}.")
            break

if day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
