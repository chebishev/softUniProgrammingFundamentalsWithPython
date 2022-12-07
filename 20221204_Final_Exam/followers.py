facebook_followers = {}

while True:

    command = input()
    if command == "Log out":
        break

    command = command.split(": ")
    event = command[0]
    username = command[1]

    if event == "New follower":
        if username not in facebook_followers.keys():
            facebook_followers[username] = {"likes": 0, "comments": 0}

    elif event == "Like":
        count = int(command[2])
        if username not in facebook_followers.keys():
            facebook_followers[username] = {"likes": 0, "comments": 0}
        facebook_followers[username]["likes"] += count

    elif event == "Comment":
        if username not in facebook_followers.keys():
            facebook_followers[username] = {"likes": 0, "comments": 1}
        else:
            facebook_followers[username]["comments"] += 1

    elif event == "Blocked":
        if username not in facebook_followers.keys():
            print(f"{username} doesn't exist.")
        else:
            del facebook_followers[username]

print(f"{len(facebook_followers)} followers")
for username in facebook_followers.keys():
    total_data = 0
    for data in facebook_followers[username].keys():
        total_data = facebook_followers[username]["likes"] + facebook_followers[username]["comments"]
    print(f"{username}: {total_data}")

# test inputs:

# New follower: George
# Like: George: 5
# New follower: George
# Log out

# Like: Katy: 3
# Comment: Katy
# New follower: Bob
# Blocked: Bob
# New follower: Amy
# Like: Amy: 4
# Log out

# Blocked: Amy
# Comment: Amy
# New follower: Amy
# Like: Tom: 5
# Like: Ellie: 5
# Log out
