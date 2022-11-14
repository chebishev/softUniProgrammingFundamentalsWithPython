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
