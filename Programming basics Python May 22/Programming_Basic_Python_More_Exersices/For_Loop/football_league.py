stadium_capacity = int(input())
fans_total = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for numbers in range(fans_total):
    sector = input()
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    else:
        sector_g += 1

sector_a_percent = sector_a / fans_total * 100
sector_b_percent = sector_b / fans_total * 100
sector_v_percent = sector_v / fans_total * 100
sector_g_percent = sector_g / fans_total * 100
all_percent = fans_total / stadium_capacity * 100

print(f'{sector_a_percent:.2f}%')
print(f'{sector_b_percent:.2f}%')
print(f'{sector_v_percent:.2f}%')
print(f'{sector_g_percent:.2f}%')
print(f'{all_percent:.2f}%')

# test input 76 10 A V V V G B A V B B
# test input 93 16 A V G G B B G B A B B B A B B A
# test input 1000 12 A A V V A G A A V G V A
