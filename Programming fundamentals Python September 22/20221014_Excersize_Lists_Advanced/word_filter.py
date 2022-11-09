some_text = input().split()
final_list = [word for word in some_text if len(word) % 2 == 0]
print(*final_list, sep="\n")

# test inputs:

# kiwi orange banana apple

# pizza cake pasta chips
