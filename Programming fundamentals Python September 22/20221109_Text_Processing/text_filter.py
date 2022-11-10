filter_words = input().split(", ")
text_string = input()

for word in filter_words:
    text_string = text_string.replace(word, "*" * len(word))

print(text_string)

# test input:

# Linux, Windows
# It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality.
# Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client
