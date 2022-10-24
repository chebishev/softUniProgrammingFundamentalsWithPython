book_shelf = input().split("&")

while True:
    command = input().split(" | ")

    if command[0] == "Done":
        break

    action = command[0]

    if action == "Add Book":
        book_name = command[1]
        if book_name not in book_shelf:
            book_shelf.insert(0, book_name)

    elif action == "Take Book":
        book_name = command[1]
        if book_name in book_shelf:
            book_shelf.remove(book_name)

    elif action == "Swap Books":
        first_book = command[1]
        second_book = command[2]
        if first_book in book_shelf and second_book in book_shelf:
            first_index = book_shelf.index(first_book)
            second_index = book_shelf.index(second_book)
            book_shelf[first_index], book_shelf[second_index] = second_book, first_book

    elif action == "Insert Book":
        book_name = command[1]
        if book_name not in book_shelf:
            book_shelf.append(book_name)

    elif action == "Check Book":
        index = int(command[1])
        if 0 <= index < len(book_shelf):
            print(book_shelf[index])

print(", ".join(book_shelf))

# test inputs:

# Don Quixote&The Great Gatsby&Moby Dick
# Add Book | Ulysses
# Take Book | Don Quixote
# Insert Book | Alice's Adventures in Wonderland
# Done

# Anna Karenina&Heart of Darkness&Catch-22&The Stranger
# Add Book | Catch-22
# Swap Books | Anna Karenina | Catch-22
# Take Book | David Copperfield
# Done

# War and Peace&Hamlet&Ulysses&Madame Bovary
# Check Book | 2
# Swap Books | Don Quixote | Ulysses
# Done
