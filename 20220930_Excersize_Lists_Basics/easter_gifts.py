gifts_list = input().split()
command = input().split()
gift = ""
index = 0
while True:
    if command[0] == "OutOfStock":
        gift = command[1]
        for gifts in range(len(gifts_list)):
            if gifts_list[gifts] == gift:
                gifts_list[gifts] = "None"
    elif command[0] == "Required":
        gift = command[1]
        index = int(command[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = gift
    elif command[0] == "JustInCase":
        gift = command[1]
        gifts_list[-1] = gift
    command = input().split()
    if command[0] == "No":
        while "None" in gifts_list:
            gifts_list.remove("None")
        print(*gifts_list, sep=" ")
        break

# test inputs:

# Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
# OutOfStock Eggs
# Required Spoon 2
# JustInCase ChocolateEgg
# No Money

# Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes
# Required Paper 8
# OutOfStock Clothes
# Required Chocolate 2
# JustInCase Hat
# OutOfStock Cable
# No Money
