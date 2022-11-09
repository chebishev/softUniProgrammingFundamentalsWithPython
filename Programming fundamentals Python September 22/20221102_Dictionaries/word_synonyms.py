commands_count = int(input())
synonyms_dict = {}
for index in range(0, commands_count * 2, 2):
    word = input()
    if word not in synonyms_dict.keys():
        synonyms_dict[word] = []
    synonyms_dict[word].append(input())

for key, value in synonyms_dict.items():
    print(f"{key} - {', '.join(value)}")

# test inputs:

# 3
# cute
# adorable
# cute
# charming
# smart
# clever

# 2
# task
# problem
# task
# assignment
