actor_name = input()
academy_points = float(input())
jury_count = int(input())
points = academy_points
for every_member in range(jury_count):
    member_name = input()
    points_given = float(input())
    points += len(member_name) * points_given / 2
    if points > 1250.5:
        break

if points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - points):.1f} more!")

# test inputs:

# Zahari Baharov
# 205
# 4
# Johnny Depp
# 45
# Will Smith
# 29
# Jet Lee
# 10
# Matthew Mcconaughey
# 39

# Sandra Bullock
# 340
# 5
# Robert De Niro
# 50
# Julia Roberts
# 40.5
# Daniel Day-Lewis
# 39.4
# Nicolas Cage
# 29.9
# Stoyanka Mutafova
# 33
