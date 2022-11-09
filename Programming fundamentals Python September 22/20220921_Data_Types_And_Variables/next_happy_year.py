year = int(input())
is_happy_year = False

while not is_happy_year:
    year += 1
    year_in_set = set()
    for i in range(len(str(year))):
        year_in_set.add(str(year)[i])

    is_happy_year = len(year_in_set) == len(str(year))

print(year)

# test inputs:

# 8989

# 1001
