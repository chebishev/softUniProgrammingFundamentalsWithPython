number_of_initial_pieces = int(input())
pianist_dictionary = {}

for index in range(number_of_initial_pieces):
    piece, composer, key = input().split("|")
    if composer not in pianist_dictionary.keys():
        pianist_dictionary[composer] = {}
    pianist_dictionary[composer][piece] = key
while True:
    command = input()
    piece_in_keys = False

    if command == "Stop":
        break

    command = command.split("|")
    action = command[0]
    piece = command[1]

    if action == "Add":
        composer = command[2]
        key = command[3]
        if composer not in pianist_dictionary.keys():
            pianist_dictionary[composer] = {}
        if piece not in pianist_dictionary[composer].keys():
            pianist_dictionary[composer][piece] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        current_composer = ""
        for composer, pieces in pianist_dictionary.items():
            if piece in pieces.keys():
                piece_in_keys = True
                current_composer = composer
        if piece_in_keys:
            pianist_dictionary[current_composer].pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = command[2]
        piece_in_keys = False
        for composer, pieces in pianist_dictionary.items():
            if piece in pieces.keys():
                piece_in_keys = True
        if piece_in_keys:
            pianist_dictionary[piece] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for composer, piece in sorted(pianist_dictionary.items()):
    print(f"{pianist_dictionary[composer]} -> Composer: {composer}, Key: {pianist_dictionary[composer][piece]}")
