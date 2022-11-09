words = input().split()
odd_dict = {}
for word in words:
    lower_word = word.lower()
    if lower_word in odd_dict.keys():
        odd_dict[lower_word] += 1
    else:
        odd_dict[lower_word] = 1
print_list = []
for keys in odd_dict.keys():
    if odd_dict[keys] % 2 != 0:
        print_list.append(keys)

print(' '.join(print_list))

# test inputs:

# Java C# PHP PHP JAVA C java

# 3 5 5 hi pi HO Hi 5 ho 3 hi pi

# a a A SQL xx a xx a A a XX c
