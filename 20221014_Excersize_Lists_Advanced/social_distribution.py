population_members = list(map(int, input().split(", ")))  # getting the input into list of integers
minimum_wealth = int(input())  # getting the minimum weight value as integer
poor = True  # boolean variable to break the While loop in case all poor elements are at minimum wealth

# First check just excludes the impossible variant from the equation, because it can't be done with these numbers
if sum(population_members) / len(population_members) < minimum_wealth:
    print("No equal distribution possible")

# second check excludes the meaningless loops, because all elements divided by the length are equal to the minimum
elif sum(population_members) / len(population_members) == minimum_wealth:
    for index in range(len(population_members)):
        population_members[index] = minimum_wealth
    print(population_members)


else:
    welthiest_element = max(population_members)  # getting the current wealthiest element
    index_of_welthiest_element = population_members.index(welthiest_element)  # getting the index of it
    while True:
        for index in range(len(population_members)):
            # if current element is under minimum wealth
            if population_members[index] < minimum_wealth:
                # if the wealthiest element have enough to spare with the minimum
                if population_members[index_of_welthiest_element] - population_members[index] >= minimum_wealth:
                    # subtracting the value from the wealthiest
                    population_members[index_of_welthiest_element] -= minimum_wealth - population_members[index]
                    # adding the value to the first element under the minimum ( the value is equal to the minimum)
                    population_members[index] = minimum_wealth
                    # getting the new welthiest element
                    welthiest_element = max(population_members)
                    # getting the index of the new welthiest element
                    index_of_welthiest_element = population_members.index(welthiest_element)
        # checking if all elements are at the minimum
        for index in range(len(population_members)):
            # if we have element under the minimum we are back to top again
            if population_members[index] < minimum_wealth:
                poor = True
                break
            # all elements are at the minimum.
            else:
                poor = False
        # we are going out of the loop
        if not poor:
            break
    # The output is modified list with poor elements at minimum and the others with whatever rest for them
    print(population_members)

# test inputs:

# 2, 3, 5, 15, 75
# 5

# 2, 3, 5, 15, 75
# 20

# 2, 3, 5, 45, 45
# 30

# 1, 1, 1, 70, 75
# 20
