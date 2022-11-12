some_text = input()

for character in range(len(some_text)):
    if some_text[character] == ":":
        emoticon = ":" + some_text[character + 1]
        print(emoticon)

# test input:

# There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)
