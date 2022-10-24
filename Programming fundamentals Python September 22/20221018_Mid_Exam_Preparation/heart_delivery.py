def zero_hearts(lst, idx):
    if lst[idx] == 0:
        return True


neighborhood = list(map(int, input().split("@")))
index = 0
last_position = 0

while True:
    command = input().split()
    action = command[0]

    if action == "Love!":
        break

    if action == "Jump":
        index += int(command[1])
        if index > len(neighborhood) - 1:
            index = 0
        if zero_hearts(neighborhood, index):
            print(f"Place {index} already had Valentine's day.")
        else:
            neighborhood[index] -= 2
            if zero_hearts(neighborhood, index):
                print(f"Place {index} has Valentine's day." )

    else:
        break
    last_position = index
print(f"Cupid's last position was {last_position}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    count = [house for house in neighborhood if house != 0]
    print(f"Cupid has failed {len(count)} places.")

# test inputs:

# 10@10@10@2
# Jump 1
# Jump 2
# Love

# 2@4@2
# Jump 2
# Jump 2
# Jump 8
# Jump 3
# Jump 1
# Love!
