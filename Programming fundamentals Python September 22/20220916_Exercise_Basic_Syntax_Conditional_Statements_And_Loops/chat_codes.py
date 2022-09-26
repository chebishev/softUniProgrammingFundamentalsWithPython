number_of_messages = int(input())
hidden_message = ""
for number in range(number_of_messages):
    chat_code = int(input())
    if chat_code == 86:
        hidden_message = "How are you?"
    elif chat_code == 88:
        hidden_message = "Hello"
    elif chat_code < 88:
        hidden_message = "GREAT!"
    else:
        hidden_message = "Bye."
    print(hidden_message)

# test inputs:

# 4
# 88
# 86
# 2
# 105

# 3
# 88
# 88
# 89
