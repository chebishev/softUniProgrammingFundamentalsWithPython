word = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = ""
for letter in word:
    if letter.lower() not in vowels:
        result += letter
print(result)

# test inputs:

# Python

# ILovePython
