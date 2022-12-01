judge_dictionary = {}

while True:

    command = input()
    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in judge_dictionary.keys():
        judge_dictionary[contest] = {username: points}
    elif username not in judge_dictionary[contest].keys():
        judge_dictionary[contest][username] = points
    else:
        if points > judge_dictionary[contest][username]:
            judge_dictionary[contest][username] = points

total_points_dictionary = {}
for contest, username in judge_dictionary.items():
    print(f"{contest}: {len(judge_dictionary[contest])} participants")
    counter = 1
    for user, points in sorted(judge_dictionary[contest].items(), key=lambda x: (-x[1], x[0])):
        print(f"{counter}. {user} <::> {points}")
        if user not in total_points_dictionary.keys():
            total_points_dictionary[user] = 0
        total_points_dictionary[user] += points
        counter += 1

print("Individual standings:")
counter = 1
for user, total_points in sorted(total_points_dictionary.items(), key=lambda x: (-x[1], x[0])):
    print(f"{counter}. {user} -> {total_points}")
    counter += 1

# test inputs:

# Peter -> Algo -> 400
# George -> Algo -> 300
# Simo -> Algo -> 200
# Peter -> DS -> 150
# Mariya -> DS -> 600
# no more time

# Peter -> OOP -> 350
# George -> OOP -> 250
# Simo -> Advanced -> 600
# George -> OOP -> 300
# Prakash -> OOP -> 300
# Prakash -> Advanced -> 250
# Ani -> JSCore -> 400
# no more time

