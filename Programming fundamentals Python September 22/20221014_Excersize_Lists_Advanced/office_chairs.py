rooms = int(input())
current_room = 0
free_chairs = 0
no_extra_chairs_needed = True
for room in range(rooms):
    command = input().split()
    chairs = command[0]
    visitors = int(command[1])
    current_room += 1
    if visitors > len(chairs):
        no_extra_chairs_needed = False
        print(f"{visitors-len(chairs)} more chairs needed in room {current_room}")
    elif len(chairs) > visitors:
        free_chairs += len(chairs) - visitors
    else:
        continue

if no_extra_chairs_needed:
    print(f"Game On, {free_chairs} free chairs left")

# test inputs:

# 4
# XXXX 4
# XX 1
# XXXXXX 3
# XXX 3

# 3
# XXXXXXX 5
# XXXX 5
# XXXXXX 8
