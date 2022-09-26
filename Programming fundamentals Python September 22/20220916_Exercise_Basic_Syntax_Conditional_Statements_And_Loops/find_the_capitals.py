word = input()
counter = 0
index = []
for letter in word:
    if letter.isupper():
        index.append(counter)
        counter += 1
    else:
        counter += 1
        continue
print(index)

# test inputs:

# pYtHoN

# CApiTAls
