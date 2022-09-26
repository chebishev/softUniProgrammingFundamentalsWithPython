detergent = int(input())
command = input()
dishes = 0
pots = 0
load = 0
total_detergent = detergent * 750

while command != "End":
    load += 1
    if load < 3:
        temp_dishes = int(command)
        dishes += temp_dishes
        total_detergent -= temp_dishes * 5
    else:
        temp_pots = int(command)
        pots += temp_pots
        total_detergent -= temp_pots * 15
        load = 0

    if total_detergent < 0:
        print(f'Not enough detergent, {abs(total_detergent)} ml. more necessary!')
        break
    command = input()
    if command == "End":
        print("Detergent was enough!")
        print(f'{dishes} dishes and {pots} pots were washed.')
        print(f"Leftover detergent {total_detergent} ml.")
        break

# test input 2 53 65 55 End
# test input 1 10 15 10 12 13 30
