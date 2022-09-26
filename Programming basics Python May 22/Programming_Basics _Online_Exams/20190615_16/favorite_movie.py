import sys
command = input()
points = 0
max_points = -sys.maxsize
chosen_movie = ''
counter = 0
while command != "STOP":
    movie_name = command
    counter += 1
    for element in movie_name:
        temp_number = ord(element)
        if 65 <= temp_number <= 90:
            points += temp_number - len(movie_name)
        elif 97 <= temp_number <= 122:
            points += temp_number - (len(movie_name) * 2)
        else:
            points += temp_number
    if points > max_points:
        max_points = points
        chosen_movie = movie_name
    if counter == 7:
        print("The limit is reached.")
        break
    points = 0
    command = input()
    if command == "Stop":
        break
print(f"The best movie for you is {chosen_movie} with {max_points} ASCII sum.")

# test input Matrix Breaking bad Legend STOP
# test input Wrong turn The maze Area 51 Night club Ice age Harry Potter Wizards
