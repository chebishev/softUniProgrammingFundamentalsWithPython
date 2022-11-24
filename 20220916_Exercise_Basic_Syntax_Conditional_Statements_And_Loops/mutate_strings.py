first_string = input()
second_string = input()
current_string = first_string
for index in range(len(first_string)):
    mutated_string = second_string[:index+1]+first_string[index+1:]
    if mutated_string == current_string:
        continue
    print(mutated_string)
    current_string = mutated_string

# test inputs:

# bubble gum
# turtle hum

# Kitty
# Doggy
