persons = int(input())
capacity = int(input())
courses = persons // capacity

if persons <= capacity:
    print(courses)
else:
    if (persons % capacity) != 0:
        courses += 1
    print(courses)

# test inputs:

# 17 3

# 4 5

# 10 5
