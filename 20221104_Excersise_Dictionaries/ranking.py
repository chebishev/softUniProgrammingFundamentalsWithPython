# getting the first row of the input strings:
command = input()

# initial dictionary which will contain contest names and their passwords
contest_dict = {}
while True:

    if command == "end of contests":
        break

    # splitting the command to two values and putting them into the dictionary on each iteration
    contest, password = command.split(':')
    if contest not in contest_dict.keys():  # add the contest as a key if it doesn't exist in the dictionary
        contest_dict[contest] = ""
    contest_dict[contest] = password   # add the password to the current contest

    # getting the input again
    command = input()

# getting the first row of the second strings input
command = input()

# this dictionary will contain Username as a key, contest as nested key, and points as value to the contest
ranking_dict = {}
while True:

    if command == "end of submissions":
        break

    # splitting the input on 4 parts and creating 4 variables
    contest, password, username, points = command.split("=>")

    # this one must be integer
    points = int(points)

    # checking if the contest is valid ( if the contest is a key in the initial dictionary (contest_dict)
    if contest in contest_dict.keys():
        # checking if the password is valid (if the password is the true value to the current contest)
        if password in contest_dict[contest]:
            # checking if the username is already a key in the new dictionary (ranking_dict)
            if username not in ranking_dict.keys():
                # if not - creating new key with the username and adding the initial points to it, as value
                ranking_dict[username] = {contest: points}
            else:
                # if we have the username as a key we are checking for contest as a nested key
                if contest in ranking_dict[username].keys():
                    # if the contest exists, we are replacing the points if they are more than the current ones
                    if points > ranking_dict[username][contest]:
                        ranking_dict[username][contest] = points
                    else:
                        # if the points are equal or less - skipping this iteration and getting the next input line
                        command = input()
                        continue
                else:
                    # if the contest doesn't exist we are adding it with the current points as initial value
                    ranking_dict[username][contest] = points
        else:
            # if the password is not corresponding with the current contest - skip the iteration, get new input line
            command = input()
            continue
    else:
        # if the contest is not in the first dictionary (contest_dict) - skip the iteration, get new input line
        command = input()
        continue
    # get new input line if all checks above are valid
    command = input()


best_user = ""  # this will contain the best user by total points
total_points = 0   # this will contain the total points of the best user
# dictionary that will contain user as a key and points as a value, which will be added on each iteration
users_total_points = {}
for username, contest in ranking_dict.items():  # getting usernames from the ranking_dict
    for contests, points in contest.items():  # getting points from each contest for the current username
        if username not in users_total_points.keys():
            # adding the username as a key to users_total_points dictionary and the points as a value
            users_total_points[username] = points
        else:
            # if the username already exists: adding the points to the existing ones in the values
            users_total_points[username] += points

for user, point in users_total_points.items():  # calculating which user has most total points
    if point > total_points:  # if the points are more than the current total_points
        best_user = user    # replace the current best user
        total_points = point   # replace the current best points
print(f"Best candidate is {best_user} with total {total_points} points.")
print("Ranking:")

for key in sorted(ranking_dict.keys()):
    print(key)   # print username in alphabetical order
    # after that it sorts the nested dictionary by value in descending order
    for contest, points in sorted(ranking_dict[key].items(), key=lambda x: x[1], reverse=True):
        print(f"#  {contest} -> {points}")  # and prints the contest corresponding to the current value

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
