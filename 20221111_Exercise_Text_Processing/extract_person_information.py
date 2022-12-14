strings_with_names = int(input())

for _ in range(strings_with_names):
    current_name = input()
    name_found = False
    age_found = False
    name = ""
    age = ""
    for character in current_name:
        if age_found and character == "*":
            age_found = False
            continue
        if name_found and character == "|":
            name_found = False
            continue
        if age_found:
            age += character
        if name_found:
            name += character
        if character == "#":
            age_found = True
        if character == "@":
            name_found = True
            continue
    age = int(age)
    print(f"{name} is {age} years old.")

# test inputs:

# 2
# Here is a name @George| and an age #18*
# Another name @Billy| #35* is his age

# 3
# random name @lilly| random digits #5*age
# @Marry| with age #19*
# here Comes @Garry|he is #48* years old
