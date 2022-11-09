lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_broken = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        expenses += helmet_price
    if fight % 3 == 0:
        expenses += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        shield_broken += 1
        expenses += shield_price
    if shield_broken == 2:
        expenses += armor_price
        shield_broken = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")

# test inputs:

# 7
# 2
# 3
# 4
# 5

# 23
# 12.50
# 21.50
# 40
# 200
