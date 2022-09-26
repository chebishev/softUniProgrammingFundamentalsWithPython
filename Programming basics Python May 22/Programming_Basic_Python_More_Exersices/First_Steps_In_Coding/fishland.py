mackerel_kg_price = float(input())
sprat_fish_kg_price = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())

bonito_kg_price = mackerel_kg_price + (mackerel_kg_price * 0.6)
bonito_sum = bonito_kg * bonito_kg_price
horse_mackerel_price = sprat_fish_kg_price + (sprat_fish_kg_price * 0.8)
horse_mackerel_sum = horse_mackerel_price * horse_mackerel_kg
mussels_sum = mussels_kg * 7.50

total = bonito_sum + horse_mackerel_sum + mussels_sum

print(f'{total:.2f}')

# mackerel - скумрия
# sprat fish - цаца
# bonito - паламуд?
# horse mackerel - сафрид
# mussels - миди

# test input 6.90 4.20 1.5 2.5 1
# test input 5.55 3.57 4.3 3.6 7
