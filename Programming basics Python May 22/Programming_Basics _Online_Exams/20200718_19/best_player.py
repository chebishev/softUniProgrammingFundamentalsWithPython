import sys
command = input()
best_player = ""
max_goals = -sys.maxsize
hat_trick = False

while command != "END":
    player_name = command
    goals = int(input())
    if goals >= 10:
        print(f"{player_name} is the best player!")
        print(f"He has scored {goals} goals and made a hat-trick !!!")
        break
    else:
        temp_goals = goals
        if temp_goals > max_goals:
            max_goals = temp_goals
            best_player = player_name
    command = input()
    if command == "END":
        if goals >= 3:
            hat_trick = True
        if hat_trick:
            print(f"{best_player} is the best player!")
            print(f"He has scored {max_goals} goals and made a hat-trick !!!")
        else:
            print(f"{best_player} is the best player!")
            print(f"He has scored {max_goals} goals.")
        break

# test input Neymar 2 Ronaldo 1 Messi 3 END
# test input Silva 5 Harry Kane 10
# test input Rooney 1 Junior 2 Paolinio 2 END
# test input Petrov 2 Drogba 11
# test input Zidane 1 Felipe 2 Johnson 4 END
