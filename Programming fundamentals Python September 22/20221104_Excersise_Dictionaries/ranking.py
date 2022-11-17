command = input()
contest_dict = {}
while True:

    if command == "end of contests":
        break

    contest, password = command.split(':')
    if contest not in contest_dict.keys():
        contest_dict[contest] = ""
    contest_dict[contest] = password

    command = input()

command = input()
ranking_dict = {}
while True:

    if command == "end of submissions":
        break
    contest, password, username, points = command.split("=>")
    points = int(points)
    if contest in contest_dict.keys():
        if password in contest_dict[contest]:
            if username not in ranking_dict.keys():
                ranking_dict[username] = {contest: points}
            else:
                if contest in ranking_dict[username].keys():
                    if points > ranking_dict[username][contest]:
                        ranking_dict[username][contest] = points
                    else:
                        command = input()
                        continue
                else:
                    ranking_dict[username][contest] = points
        else:
            command = input()
            continue
    else:
        command = input()
        continue
    command = input()

best_user = ""
total_points = 0
users_total_points = {}
for username, contest in ranking_dict.items():
    for contests, points in contest.items():
        if username not in users_total_points.keys():
            users_total_points[username] = points
        else:
            users_total_points[username] += points
for user, point in users_total_points.items():
    if point > total_points:
        best_user = user
        total_points = point
print(f"Best candidate is {best_user} with total {total_points} points.")
print("Ranking:")

for key in sorted(ranking_dict.keys()):
    print(key)
    for contest, points in sorted(ranking_dict[key].items(), key=lambda x: x[1], reverse=True):
        print(f"#  {contest} -> {points}")

# test inputs:

# Part One Interview:success
# JS Fundamentals:fundExam
# C# Fundamentals:fundPass
# Algorithms:fun
# end of contests
# C# Fundamentals=>fundPass=>Tanya=>350
# Algorithms=>fun=>Tanya=>380
# Part One Interview=>success=>Nikola=>120
# Java Basics Exam=>wrong_pass=>Teo=>400
# Part One Interview=>success=>Tanya=>220
# OOP Advanced=>password123=>Kay=>231
# C# Fundamentals=>fundPass=>Tanya=>250
# C# Fundamentals=>fundPass=>Nikola=>200
# JS Fundamentals=>fundExam=>Tanya=>400
# end of submissions

# Java Advanced:funpass
# Part Two Interview:success
# Math Concept:asdasd
# Java Web Basics:forrF
# end of contests
# Math Concept=>ispass=>Monika=>290
# Java Advanced=>funpass=>Simona=>400
# Part Two Interview=>success=>Drago=>120
# Java Advanced=>funpass=>Petyr=>90
# Java Web Basics=>forrF=>Simona=>280
# Part Two Interview=>success=>Petyr=>0
# Math Concept=>asdasd=>Drago=>250
# Part Two Interview=>success=>Simona=>200
# end of submissions
