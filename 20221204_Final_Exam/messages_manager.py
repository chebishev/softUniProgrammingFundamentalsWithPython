max_capacity = int(input())
messages_dictionary = {}

while True:

    command = input()
    if command == "Statistics":
        break

    command = command.split("=")

    action = command[0]

    if action == "Add":
        username = command[1]
        sent = int(command[2])
        received = int(command[3])
        if username not in messages_dictionary.keys():
            messages_dictionary[username] = {}
            messages_dictionary[username]["sent"] = sent
            messages_dictionary[username]["received"] = received

    elif action == "Message":
        sender = command[1]
        receiver = command[2]
        if (sender and receiver) in messages_dictionary.keys():
            messages_dictionary[sender]["sent"] += 1
            if (messages_dictionary[sender]["sent"] + messages_dictionary[sender]["received"]) == max_capacity:
                print(f"{sender} reached the capacity!")
                del messages_dictionary[sender]
            messages_dictionary[receiver]["received"] += 1
            if (messages_dictionary[receiver]["sent"] + messages_dictionary[receiver]["received"]) == max_capacity:
                print(f"{receiver} reached the capacity!")
                del messages_dictionary[receiver]

    elif action == "Empty":
        username = command[1]
        if username == "All":
            messages_dictionary = {}
            continue
        del messages_dictionary[username]

print(f"Users count: {len(messages_dictionary)}")
for key in messages_dictionary.keys():
    messages_count = messages_dictionary[key]["sent"] + messages_dictionary[key]["received"]
    print(f"{key} - {messages_count}")

# test inputs:

# 10
# Add=Berg=9=0
# Add=Kevin=0=0
# Message=Berg=Kevin
# Add=Mark=5=4
# Statistics

# 20
# Add=Mark=3=9
# Add=Berry=5=5
# Add=Clark=4=0
# Empty=Berry
# Add=Blake=9=3
# Add=Michael=3=9
# Add=Amy=9=9
# Message=Blake=Amy
# Message=Michael=Amy
# Statistics

# 12
# Add=Bonnie=3=5
# Add=Johny=4=4
# Empty=All
# Add=Bonnie=3=3
# Statistics

# https://softwareuniversity-my.sharepoint.com/:w:/g/personal/joana_veskova_students_softuni_bg/EY2ZKgffqbpGltGLO55ndQYBfTTb3N5LKaTyZIYx9IXtSA?e=9MzVWl
