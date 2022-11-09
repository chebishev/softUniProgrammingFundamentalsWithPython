budget = int(input())
command = input()

while command != "End":
    expense = int(command)
    if expense > budget:
        print("You went in overdraft!")
        break
    budget -= expense
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break

# test inputs:
# 100
# 5
# End

# 50
# 25
# 20
# 10