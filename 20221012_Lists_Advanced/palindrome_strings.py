words = input().split()
palindrome = input()
final_list = [word for word in words if word == word[::-1]]
counter = final_list.count(palindrome)
print(final_list)
print(f"Found palindrome {counter} times")

# test inputs:

# wow father mom wow shirt stats
# wow

# hey how you doin? lol
# mom
