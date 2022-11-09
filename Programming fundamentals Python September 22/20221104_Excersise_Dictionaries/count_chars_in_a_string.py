text_string = input()
count_dictionary = {}

for char in text_string:
    if char == " ":
        continue
    if char not in count_dictionary.keys():
        count_dictionary[char] = 0
    count_dictionary[char] += 1

for key, value in count_dictionary.items():
    print(f"{key} -> {value}")

# test inputs:

# text

# text text text
