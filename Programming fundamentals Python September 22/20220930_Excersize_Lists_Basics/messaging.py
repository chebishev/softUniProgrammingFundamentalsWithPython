coded_message = input().split()
decoding_string = input()

index_list = []
for numbers in coded_message:
    current_index = 0
    for number in numbers:
        current_index += int(number)
    index_list.append(current_index)

final_string = ""
for index in range(len(index_list)):
    string_index = index_list[index]
    valid_index = len(decoding_string)
    while string_index >= valid_index:
        string_index -= valid_index
    if decoding_string[string_index].isdigit():
        continue
    else:
        final_string += decoding_string[string_index]
        decoding_string = decoding_string.replace(decoding_string[string_index], "", 1)
print(final_string)

# test inputs:

# 9992 562 8933
# This is some message for you

# 2 122 1123 1321 9 17211
# 87j973u59dg37e725!
