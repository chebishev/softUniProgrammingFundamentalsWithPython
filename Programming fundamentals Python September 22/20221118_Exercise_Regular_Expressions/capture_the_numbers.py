import re

line = input()
while line:

    search_pattern = r"\d+"
    result = re.findall(search_pattern, line)
    for number in result:
        print(number, end=" ")
    line = input()

# test inputs:

# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45

# 123a456
# 789b987
# 654c321
# 0

# Let's go11!!!11!
# Okey!1!
