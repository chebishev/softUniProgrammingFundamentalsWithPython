player_one = input()
player_two = input()
command = input()
points_one = 0
points_two = 0

while command != "End of game":
    first_card = int(command)
    second_card = int(input())
    if first_card > second_card:
        points_one += first_card - second_card
    elif second_card > first_card:
        points_two += second_card - first_card
    else:
        print("Number wars!")
        first_card = int(input())
        second_card = int(input())
        if first_card > second_card:
            print(f"{player_one} is winner with {points_one} points")
            break
        elif second_card > first_card:
            print(f"{player_two} is winner with {points_two} points")
            break
    command = input()
    if command == "End of game":
        print(f"{player_one} has {points_one} points")
        print(f"{player_two} has {points_two} points")
        break

# test input Desi Niki 7 5 3 4 3 3 5 3
# test input Elena Simeon 6 3 2 5 8 9 End of game
# test input Aleks Georgi 4 5 3 2 4 3 4 4 5 2
