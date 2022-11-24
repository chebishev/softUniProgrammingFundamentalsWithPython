operations = int(input())
parking_users = {}

for index in range(operations):
    command = input().split()
    operation = command[0]
    if operation == "register":
        username, license_plate_number = command[1], command[2]
        if username not in parking_users.keys():
            parking_users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_users[username]}")
    elif operation == "unregister":
        username = command[1]
        if username not in parking_users.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking_users[username]
            print(f"{username} unregistered successfully")

for key, value in parking_users.items():
    print(f"{key} => {value}")


# test inputs:

# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy

# 4
# register Jony AA4132BB
# register Jony AA4132BB
# register Linda AA9999BB
# unregister Jony

# 6
# register Jacob MM1111XX
# register Anthony AB1111XX
# unregister Jacob
# register Joshua DD1111XX
# unregister Lily
# register Samantha AA9999BB
