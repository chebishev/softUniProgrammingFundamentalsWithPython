number_of_initial_pieces = int(input())
pianist_dictionary = {}

for index in range(number_of_initial_pieces):
    piece, composer, key = input().split("|")
    pianist_dictionary[piece] = {}
    pianist_dictionary[piece][composer] = key
while True:

    command = input()
    if command == "Stop":
        break

    command = command.split("|")
    action = command[0]
    piece = command[1]

    if action == "Add":
        composer = command[2]
        key = command[3]
        if piece not in pianist_dictionary.keys():
            pianist_dictionary[piece] = {}
            if composer not in pianist_dictionary[piece].keys():
                pianist_dictionary[piece][composer] = key
                print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        if piece in pianist_dictionary.keys():
            pianist_dictionary.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = command[2]
        if piece in pianist_dictionary.keys():
            for composer in pianist_dictionary[piece].keys():
                if composer in pianist_dictionary[piece].keys():
                    pianist_dictionary[piece][composer] = new_key
                    print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, composer in pianist_dictionary.items():
    for key, value in sorted(composer.items()):
        print(f"{piece} -> Composer: {key}, Key: {value}")

# test inputs:

# 3
# Fur Elise|Beethoven|A Minor
# Moonlight Sonata|Beethoven|C# Minor
# Clair de Lune|Debussy|C# Minor
# Add|Sonata No.2|Chopin|B Minor
# Add|Hungarian Rhapsody No.2|Liszt|C# Minor
# Add|Fur Elise|Beethoven|C# Minor
# Remove|Clair de Lune
# ChangeKey|Moonlight Sonata|C# Major
# Stop

# 4
# Eine kleine Nachtmusik|Mozart|G Major
# La Campanella|Liszt|G# Minor
# The Marriage of Figaro|Mozart|G Major
# Hungarian Dance No.5|Brahms|G Minor
# Add|Spring|Vivaldi|E Major
# Remove|The Marriage of Figaro
# Remove|Turkish March
# ChangeKey|Spring|C Major
# Add|Nocturne|Chopin|C# Minor
# Stop