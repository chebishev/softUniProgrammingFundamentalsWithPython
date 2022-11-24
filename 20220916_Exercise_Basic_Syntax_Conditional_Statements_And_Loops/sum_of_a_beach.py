words = input()
lower_words = words.lower()
temp_word = ""
counter = 0
for letter in lower_words:
    temp_word += letter
    if "sun" in temp_word or \
            "sand" in temp_word or \
            "water" in temp_word or \
            "fish" in temp_word:
        counter += 1
        temp_word = ""
print(counter)

# test inputs

# WAtErSlIde

# GolDeNSanDyWateRyBeaChSuNN

# gOfIshsunesunFiSh

# cItYTowNcARShoW
