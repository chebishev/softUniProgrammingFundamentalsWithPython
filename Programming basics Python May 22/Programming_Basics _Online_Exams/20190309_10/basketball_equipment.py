annual_tax = int(input())

sneakers_price = annual_tax * 0.60
equip_price = sneakers_price * 0.80
ball_price = equip_price / 4
accessories = ball_price / 5
total = annual_tax + equip_price + sneakers_price + ball_price + accessories

print(f"{total:.2f}")

# test input 320
# test input 550
# test input 230
