food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
guinea_weight = float(input()) * 1000
enough = True
for day in range(1, 31):
    food_quantity -= 300
    if food_quantity <= 0:
        enough = False
        break
    if day % 2 == 0:
        hay_quantity -= 0.05 * food_quantity
        if hay_quantity <= 0:
            enough = False
            break
    if day % 3 == 0:
        cover_quantity -= guinea_weight / 3
        if cover_quantity <= 0:
            enough = False
            break
if not enough:
    print(f"Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity/1000:.2f}, Hay: {hay_quantity/1000:.2f}, Cover: {cover_quantity/1000:.2f}.")

# test inputs:

# 10
# 5
# 5.2
# 1

# 1
# 1.5
# 3
# 1.5

# 9
# 5
# 5.2
# 1
