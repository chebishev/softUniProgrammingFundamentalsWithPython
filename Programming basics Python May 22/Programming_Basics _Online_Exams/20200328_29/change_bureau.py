bitcoin_quantity = int(input())
yuan_quantity = float(input())
# commission 1-5%
commission = float(input()) / 100

# bitcoin to lev = 1168
# yuan to dollar = 0.15
# dollar to lev = 1.76
# euro to lev = 1.95

yuan_to_lev = (yuan_quantity * 0.15) * 1.76
bitcoin_to_lev = bitcoin_quantity * 1168
total_in_euro = (yuan_to_lev + bitcoin_to_lev) / 1.95
total = total_in_euro - (total_in_euro * commission)

print(f"{total:.2f}")

# test input 1 5 5
# test input 20 5678 2.4
