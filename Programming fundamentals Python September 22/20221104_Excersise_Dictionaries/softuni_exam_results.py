softuni_exam = {}
languages = {}
banned_users = {}
while True:

    command = input()
    if command == "exam finished":
        break

    current_submission = command.split("-")
    user = current_submission[0]
    language = current_submission[1]

    if language == "banned":
        banned_users[user] = True
    else:
        points = int(current_submission[2])
        if user not in softuni_exam.keys():
            softuni_exam[user] = {}
            softuni_exam[user][language] = points
        else:
            if language not in softuni_exam[user]:
                softuni_exam[user] = {language: points}
                current_points = softuni_exam[user][language]
                if points > current_points:
                    current_points = points
        if language not in languages.keys():
            languages[language] = 1
        else:
            languages[language] += 1

print("Results:")
for key, values in softuni_exam.items():
    check_max_points = []
    for value in values.values():
        check_max_points.append(value)
    if key not in banned_users.keys():
        print(f"{key} | {max(check_max_points)}")
print("Submissions:")
for key, value in languages.items():
    print(f"{key} - {value}")

# 80/100
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
