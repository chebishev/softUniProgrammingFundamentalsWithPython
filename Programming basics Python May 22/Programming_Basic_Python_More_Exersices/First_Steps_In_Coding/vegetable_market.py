vegetables_kg_price = float(input())
fruits_kg_price = float(input())
vegetables_kg_total = int(input())
fruits_kg_total = int(input())

vegetables_price = vegetables_kg_price * vegetables_kg_total
fruits_price = fruits_kg_price * fruits_kg_total

total = (vegetables_price + fruits_price) / 1.94

print(f'{total:.2f}')

# test input 0.194 19.4 10 10
# test input 1.5 2.5 10 10
