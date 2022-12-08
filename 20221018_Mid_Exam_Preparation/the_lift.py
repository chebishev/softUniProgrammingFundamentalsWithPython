def lift_is_full(wagons_list):
    if len(wagons_list) * 4 < sum(wagons_list):
        return False
    elif len(wagons_list) * 4 == sum(wagons_list):
        return True


people_waiting = int(input())
lift_initial_state = list(map(int, input().split()))

for index in range(len(lift_initial_state)):
    while people_waiting and lift_initial_state[index] < 4:
        lift_initial_state[index] += 1
        people_waiting -= 1
        if not people_waiting and not lift_is_full(lift_initial_state):
            print(f"The lift has empty spots!\n", *lift_initial_state, end=" ")
            break
        elif people_waiting and lift_is_full(lift_initial_state):
            print(f"There isn't enough space! {people_waiting} people in a queue!\n", *lift_initial_state, end=" ")
            break
        elif not people_waiting and lift_is_full(lift_initial_state):
            print(*lift_initial_state, end=" ")
            break

# test inputs:

# 15
# 0 0 0 0

# 20
# 0 2 0
