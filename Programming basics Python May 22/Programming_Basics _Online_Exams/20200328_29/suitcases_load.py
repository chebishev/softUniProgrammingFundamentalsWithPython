trunk_capacity = float(input())
command = input()
load_counter = 0

while command != "End":
    luggage_volume = float(command)
    load_counter += 1
    if load_counter % 3 == 0:
        luggage_volume *= 1.10
    trunk_capacity -= luggage_volume
    if trunk_capacity <= 0:
        print("No more space!")
        load_counter -= 1
        break
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break

print(f"Statistic: {load_counter} suitcases loaded.")

# test input 550 100 252 72 End
# test input 700.5 180 340.6 126 220
# test input 1200.2 260 380.5 125.6 305 End
