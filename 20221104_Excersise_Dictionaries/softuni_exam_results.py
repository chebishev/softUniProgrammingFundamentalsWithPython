softuni_exam = {}  # main dictionary
languages = {}  # this contains only the languages as keys and the values are counters
banned_users = []  # if the banned user is more than one it will be checked at the and will be excluded from the print
while True:

    command = input()
    if command == "exam finished":
        break

    current_submission = command.split("-")  # it splits the input on 2 or 3 parts
    user = current_submission[0]
    language = current_submission[1]

    if language == "banned":
        banned_users.append(user)  # adding the user in the list with banned users
    else:
        points = int(current_submission[2])
        if user not in softuni_exam.keys():   # checking if the user is one of the keys
            softuni_exam[user] = {}   # adding the user with empty dictionary as a value
            softuni_exam[user][language] = points  # "appending" the data in the nested dictionary
        else:
            if language not in softuni_exam[user]:   # check if the language exists as a key in the nested dictionary
                softuni_exam[user] = {language: points}   # adding the language and the points in the dictionary
            else:
                current_points = softuni_exam[user][language]  # getting the current value of the points
                if points > current_points:
                    softuni_exam[user][language] = points
        if language not in languages.keys():
            languages[language] = 1
        else:
            languages[language] += 1

print("Results:")
for key, values in softuni_exam.items():
    check_max_points = []
    for value in values.values():
        check_max_points.append(value)
    if key not in banned_users:
        print(f"{key} | {max(check_max_points)}")
print("Submissions:")
for key, value in languages.items():
    print(f"{key} - {value}")

# test inputs:

# Peter-Java-84
# George-C#-84
# George-C#-70
# Katy-C#-94
# exam finished

# Peter-Java-91
# George-C#-84
# Katy-Java-90
# Katy-C#-50
# Katy-banned
# exam finished
