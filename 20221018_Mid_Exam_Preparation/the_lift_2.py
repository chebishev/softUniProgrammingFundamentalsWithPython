people_wait = int(input())
lift_initial_state = [int(x) for x in input().split()]
lift_full = False
no_people = False
for wagon in range(len(lift_initial_state)):
    if no_people or lift_full:
        break
    while people_wait:
        if lift_initial_state[wagon] < 4:
            lift_initial_state[wagon] += 1
            people_wait -= 1
            if people_wait == 0:
                no_people = True
        if lift_initial_state[wagon] == 4:
            if wagon == len(lift_initial_state) - 1:
                lift_full = True
            break

if lift_full and people_wait:
    print(f"There isn't enough space! {people_wait} people in a queue!")
elif not people_wait and not lift_full:
    print("The lift has empty spots!")
print(*lift_initial_state, end=" ")
