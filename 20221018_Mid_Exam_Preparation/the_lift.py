def all_wagons_full(lst):
    if sum(lst) == 4 * len(lst):
        return True


people_waiting = int(input())
current_state = list(map(int, input().split()))
has_empty_slots = False
while True:
    if people_waiting <= 0 and sum(current_state) < 4 * len(current_state):
        has_empty_slots = True
        break
    elif people_waiting <= 0:
        break
    for wagon in range(len(current_state)):
        free_space = 4 - current_state[wagon]
        if people_waiting < free_space:
            current_state[wagon] += people_waiting
            people_waiting = 0
        else:
            current_state[wagon] += free_space
            people_waiting -= free_space
        if people_waiting <= 0 and sum(current_state) < 4 * len(current_state):
            has_empty_slots = True
            break
        elif all_wagons_full(current_state):
            break
        if people_waiting <= 0:
            break
    if all_wagons_full(current_state):
        break
if has_empty_slots:
    print(f"The lift has empty spots!\n", *current_state, sep=" ")
else:
    print(f"There isn't enough space! {people_waiting} people in a queue!\n", *current_state, sep=" ")
