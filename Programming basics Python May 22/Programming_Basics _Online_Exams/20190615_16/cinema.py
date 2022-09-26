hall_capacity = int(input())
command = input()
free_spots = 0
total = 0
while command != "Movie time!":
    people = int(command)
    free_spots += people
    if free_spots > hall_capacity:
        print("The cinema is full.")
        break
    total += people * 5
    if people % 3 == 0:
        total -= 5
    command = input()
    if command == "Movie time!":
        diff = hall_capacity - free_spots
        print(f"There are {diff} seats left in the cinema.")
        break

print(f"Cinema income - {total} lv.")

# test input 60 10 6 3 20 15 Movie time!
# test input 50 15 10 10 15 5
# test input 100 10 10 10 10 10 10 10 10 10 10 Movie Time!
