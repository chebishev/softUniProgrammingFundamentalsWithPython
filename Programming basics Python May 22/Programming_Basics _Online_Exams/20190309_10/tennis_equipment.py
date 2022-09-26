from math import floor
from math import ceil
tennis_racket_price = float(input())
tennis_racket_count = int(input())
sneakers_pairs_count = int(input())

sneakers_price = sneakers_pairs_count * (tennis_racket_price / 6)
total_price = sneakers_price + (tennis_racket_price * tennis_racket_count)
other_equipment = total_price * 0.20
total_price += other_equipment
djokovich_pays = total_price / 8
sponsors_pay = total_price - djokovich_pays

print(f"Price to be paid by Djokovic {floor(djokovich_pays)}")
print(f"Price to be paid by sponsors {ceil(sponsors_pay)}")

# test input 850 4 2
# test input 386 7 4
