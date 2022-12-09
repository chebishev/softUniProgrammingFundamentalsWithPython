first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))
third_row = list(map(int, input().split()))

row_1, row_2, row_3 = set(first_row), set(second_row), set(third_row)
col_1 = {first_row[0], second_row[0], third_row[0]}
col_2 = {first_row[1], second_row[1], third_row[1]}
col_3 = {first_row[2], second_row[2], third_row[2]}
diag_1 = {first_row[0], second_row[1], third_row[2]}
diag_2 = {first_row[2], second_row[1], third_row[0]}

no_winner = True

for index in range(1, 3):
    if row_1 == {index} or row_2 == {index} or row_3 == {index} or \
            col_1 == {index} or col_2 == {index} or col_3 == {index} or \
            diag_1 == {index} or diag_2 == {index}:
        if index == 1:
            print("First player won")
            no_winner = False
            break
        else:
            print("Second player won")
            no_winner = False
            break

if no_winner:
    print("Draw!")