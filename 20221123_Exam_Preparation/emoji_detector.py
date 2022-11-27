import re

text = input()

emoji_pattern = r"(\*{2}|[:]{2})([A-Z][a-z]{2,})\1"
emojis = re.findall(emoji_pattern, text)
valid_emojis = []
counter = 0

digits_pattern = r"\d"
all_digits = re.findall(digits_pattern, text)
cool_threshold = 1

for digit in all_digits:
    cool_threshold *= int(digit)

print(f"Cool threshold: {cool_threshold}")

for emoji in emojis:
    current_coolness = 0
    for character in emoji[1]:
        if character == "*" or character == ":":
            continue
        else:
            current_coolness += ord(character)

    if current_coolness >= cool_threshold:
        valid_emojis.append(emoji[0]+emoji[1]+emoji[0])
    counter += 1

print(f"{counter} emojis found in the text. The cool ones are:")
print('\n'.join(valid_emojis))

# test inputs:

# In the Sofia Zoo there are 311 animals in total! ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:,
# 12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::. ::Mooning:: **Shy**

# 5, 4, 3, 2, 1, go! The 1-th consecutive banana-eating contest has begun! ::Joy:: **Banana** ::Wink:: **Vali**
# ::valid_emoji::

# It is a long established fact that 1 a reader will be distracted by 9 the readable content of a page when looking
# at its layout. The point of using ::LoremIpsum:: is that it has a more-or-less normal 3 distribution of 8 letters,
# as opposed to using 'Content here, content 99 here', making it look like readable **English**.
