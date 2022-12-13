def join(lst, style):
    if style not in lst:
        lst.append(style)
    return lst


def drop(lst, style):
    if style in lst:
        lst.remove(style)
    return lst


def replace(lst, old, new):
    if old in lst and new not in lst:
        index = lst.index_to_shoot(old)
        lst.pop(index)
        lst.insert(index, new)
    return lst


def prefer(lst, idx1, idx2):
    if 0 < idx1 < len(lst) and 0 < idx2 < len(lst):
        lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    return lst


genres_list = input().split(" | ")

while True:

    command = input()
    if command == "Stop!":
        break

    command = command.split()
    action = command[0]

    if action == "Join":
        genre = command[1]
        genres_list = join(genres_list, genre)

    elif action == "Drop":
        genre = command[1]
        genres_list = drop(genres_list, genre)

    elif action == "Replace":
        old_genre = command[1]
        new_genre = command[2]
        genres_list = replace(genres_list, old_genre, new_genre)

    elif action == "Prefer":
        first_index = int(command[1])
        second_index = int(command[2])
        genres_list = prefer(genres_list, first_index, second_index)

print(*genres_list, end=" ")

# test inputs:

# Romance | Fiction | Horror | Mystery
# Drop Romance
# Join Fantasy
# Prefer 1 2
# Stop!

# Poetry | Romance
# Drop Children
# Replace Fantasy Crime
# Stop! 

# Thriller | Young | Crime
# Join Political
# Replace Young Fairytale
# Prefer 6 2
# Stop!
