number = float(input())

if number == 0:
    print("zero")

elif 0 < abs(number) < 1:
    print("small ", end='')
    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
elif abs(number) > 1000000:
    print('large ', end='')
    if number > 1:
        print("positive")
    elif number < -1:
        print("negative")
else:
    if number > 0:
        print("positive")
    else:
        print("negative")

# test inputs:
# 25
# 0.7
# 435247392.921
# -0.005
# -103.21
# -358583355123.001
