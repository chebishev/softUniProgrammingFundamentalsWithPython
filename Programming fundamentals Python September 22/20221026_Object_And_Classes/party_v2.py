class Party:

    people = []

    def __init__(self):
        pass


while True:

    command = input()

    if command == "End":
        break

    Party.people.append(command)

print(f"Going: {', '.join(Party.people)}")
print(f"Total: {len(Party.people)}")

# test inputs:

# Peter
# John
# Katy
# End

# Sam
# Eddy
# Edd
# Kris
# End
