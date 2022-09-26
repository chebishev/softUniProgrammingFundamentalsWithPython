men_count = int(input())
women_count = int(input())
max_tables = int(input())


for men in range(1, men_count+1):
    for women in range(1, women_count+1):
        if max_tables == 0:
            break
        print(f"({men} <-> {women})", end=" ")
        max_tables -= 1
        if men == men_count and women_count == women:
            break

# test input 2 2 6
# test input 2 2 3
# test input 5 8 40
