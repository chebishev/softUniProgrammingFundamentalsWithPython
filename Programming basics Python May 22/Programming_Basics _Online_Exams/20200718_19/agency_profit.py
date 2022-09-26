company_name = input()
adult_tickets = int(input())
kids_tickets = int(input()) # 70% discount
price_per_adult_ticket = float(input())
tax = float(input())

all_tickets_price = (adult_tickets * price_per_adult_ticket) + kids_tickets * (price_per_adult_ticket * 0.30)
profit = all_tickets_price + tax * (adult_tickets + kids_tickets)
profit *= 0.20

print(f'The profit of your agency from {company_name} tickets is {profit:.2f} lv.')

# test input WizzAir 15 5 120 40
# test input Ryanair 60 23 158.96 39.12
