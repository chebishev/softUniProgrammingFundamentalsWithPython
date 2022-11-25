import re

text_string = input()

pattern = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
search_match = re.findall(pattern, text_string)
matched_dictionary = {}
if len(search_match):
    for pair in search_match:
        word = pair[1]
        mirrored_word = pair[2]
        if word == mirrored_word[::-1]:
            matched_dictionary[word] = mirrored_word
else:
    print("No word pairs found!")

valid_pairs = len(search_match)
if valid_pairs:
    print(f"{valid_pairs} word pairs found!")
if len(matched_dictionary):
    print("The mirror words are:")
    counter = 0
    for key, value in matched_dictionary.items():
        counter += 1
        if counter < len(matched_dictionary):
            print(f"{key} <=> {value}", end=", ")
        else:
            print(f"{key} <=> {value}")
else:
    print("No mirror words!")

# test inputs:

# @mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r

# #po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@

# #lol#lol# @#God@@doG@# #abC@@Cba# @Xyu@#uyX#
