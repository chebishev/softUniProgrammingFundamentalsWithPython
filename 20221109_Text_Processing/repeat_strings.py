string_for_multiplication = input().split()
final_list = []
for word in string_for_multiplication:
    final_list.append(word * len(word))
print("".join(final_list))

# test inputs:

# hi abc add

# work

# ball
