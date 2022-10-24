initial_text = input()
cool_threshold = 1
for digit in initial_text:
    if digit.isdigit():
        cool_threshold *= int(digit)
print(f"Cool threshold: {cool_threshold}")
initial_list = initial_text.split()

valid_emoji_list = []
for item in initial_list:
    if item[-1] == "." or item[-1] == ",":
        item = item[0:-1:]
    if item[0:2:] == "::" and item[:-3:-1] == "::" \
            or item[0:2:] == "**" and item[:-3:-1] == "**":
        if item[2].isupper():
            if len(item) > 6:
                if item[3:-3:].isalpha() and item[3:-3:].islower():
                    valid_emoji_list.append(item)

cool_emoji_list = []
sum_ascii = 0
for emoji in valid_emoji_list:
    for character in emoji:
        sum_ascii += ord(character)
    if sum_ascii > cool_threshold:
        cool_emoji_list.append(emoji)
        sum_ascii = 0
print(f"{len(valid_emoji_list)} emojis found in the text. The cool ones are: ", *cool_emoji_list, sep="\n")

# 20/100

# test inputs:

# In the Sofia Zoo there are 311 animals in total! ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::. ::Mooning:: **Shy**

# 5, 4, 3, 2, 1, go! The 1-th consecutive banana-eating contest has begun! ::Joy:: **Banana** ::Wink:: **Vali** ::valid_emoji::

# It is a long established fact that 1 a reader will be distracted by 9 the readable content of a page when looking at its layout. The point of using ::LoremIpsum:: is that it has a more-or-less normal 3 distribution of 8 letters, as opposed to using 'Content here, content 99 here', making it look like readable **English**.
