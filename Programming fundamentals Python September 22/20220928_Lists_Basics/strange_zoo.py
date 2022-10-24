my_list = []
for animal in range(3):
    current_part = input()
    my_list.append(current_part)

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)

# test inputs:

# my tail
# my body seems on place
# my head is on the wrong end!

# tail
# body
# head

# T
# B
# H