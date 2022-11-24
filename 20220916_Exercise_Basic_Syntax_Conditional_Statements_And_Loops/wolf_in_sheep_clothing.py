animals = input()
reverted_animals = animals[::-1]
list_animals = reverted_animals.split(" ,")
index = 0
for animal in list_animals:
    if animal == "flow":
        if index == 0:
            print("Please go away and stop eating my sheep")
            break
        else:
            print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
            break
    else:
        index += 1

# test inputs:

# sheep, sheep, wolf

# wolf, sheep, sheep, sheep, sheep, sheep
