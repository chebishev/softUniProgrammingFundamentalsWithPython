people_in_fitness = int(input())
back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_shake = 0
protein_bar = 0

for people in range(people_in_fitness):
    activity = input()

    if activity == "Back":
        back_count += 1
    elif activity == "Chest":
        chest_count += 1
    elif activity == "Legs":
        legs_count += 1
    elif activity == "Abs":
        abs_count += 1
    elif activity == "Protein shake":
        protein_shake += 1
    else:
        protein_bar += 1

total_workout = back_count + chest_count + legs_count + abs_count
total_buyers = protein_bar + protein_shake
workout_percent = total_workout / people_in_fitness * 100
buyers_percent = total_buyers / people_in_fitness * 100
print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{workout_percent:.2f}% - work out")
print(f"{buyers_percent:.2f}% - protein")

# test inputs:

# 10
# Back
# Chest
# Legs
# Abs
# Protein shake
# Protein bar
# Protein shake
# Protein bar
# Legs
# Abs

# 7
# Chest
# Back
# Legs
# Legs
# Abs
# Protein shake
# Protein bar