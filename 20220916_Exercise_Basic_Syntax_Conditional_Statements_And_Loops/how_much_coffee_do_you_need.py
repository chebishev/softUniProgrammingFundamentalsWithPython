command = ""
coffee_counter = 0

while command != "END":
    command = input()
    if command == "END":
        break
    if command.lower() == "cat" or \
            command.lower() == "dog" or \
            command.lower() == "movie" or \
            command.lower() == "coding":
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2
    else:
        continue

if coffee_counter <= 5:
    print(coffee_counter)
else:
    print("You need extra sleep")

# test inputs:

# dog
# CAT
# gaming
# END

# movie
# CODING
# MOVIE
# CLEANING
# cat
# END
