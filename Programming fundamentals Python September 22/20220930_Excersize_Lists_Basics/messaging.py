list_numbers = input().split()
string = input()
list_string = []
list_indexes = []
index = 0
message = ""
for item in list_numbers:
    for number in item:
        current_number = int(number)
        index += current_number
    list_indexes.append(index)
    index = 0

for character in string:
    list_string.append(character)

for indexes in list_indexes:
    current_index = int(indexes)
    while current_index > len(list_string):
        current_index -= len(list_string)
    message += list_string.pop(current_index)
print(message)

# 83/100

# test inputs:

# 9992 562 8933
# This is some message for you

# 2 122 1123 1321 9 17211
# 87j973u59dg37e725!
