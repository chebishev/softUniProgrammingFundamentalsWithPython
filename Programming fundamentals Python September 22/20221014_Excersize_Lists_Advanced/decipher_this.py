secret_message = input().split()
readable_message = []

for word in secret_message:
    ord_as_string = ""
    current_word = []
    for symbol in word:
        if symbol.isdigit():
            ord_as_string += symbol
        else:
            current_word.append(symbol)
    ord_as_string = int(ord_as_string)
    current_word.insert(0, chr(ord_as_string))
    if len(current_word) > 2:
        current_word[1], current_word[-1] = current_word[-1], current_word[1]
    readable_message.append("".join(current_word))
print(*readable_message)

# test inputs:

# 72olle 103doo 100ya

# 82yade 115te 103o
