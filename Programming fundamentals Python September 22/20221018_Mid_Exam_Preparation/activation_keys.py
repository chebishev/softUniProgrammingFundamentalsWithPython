raw_key = input()

while True:
    command = input().split(">>>")
    action = command[0]

    if action == "Generate":
        print(f"Your activation key is: {raw_key}")
        break

    if action == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        transformation = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if transformation == "Upper":
            upper = raw_key[start_index:end_index].upper()
            raw_key = raw_key.replace(raw_key[start_index:end_index], upper)
        else:
            lower = raw_key[start_index:end_index].lower()
            raw_key = raw_key.replace(raw_key[start_index:end_index], lower)
        print(raw_key)
    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_key = raw_key.replace(raw_key[start_index:end_index], "")
        print(raw_key)

# test inputs:

# abcdefghijklmnopqrstuvwxyz
# Slice>>>2>>>6
# Flip>>>Upper>>>3>>>14
# Flip>>>Lower>>>5>>>7
# Contains>>>def
# Contains>>>deF
# Generate

# 134softsf5ftuni2020rockz42
# Slice>>>3>>>7
# Contains>>>-rock
# Contains>>>-uni-
# Contains>>>-rocks
# Flip>>>Upper>>>2>>>8
# Flip>>>Lower>>>5>>>11
# Generate
