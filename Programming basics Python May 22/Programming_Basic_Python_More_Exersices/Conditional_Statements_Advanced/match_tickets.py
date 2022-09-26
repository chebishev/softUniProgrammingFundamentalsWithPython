budget = float(input())
category = input()
people_in_the_group = int(input())
transport = 0
vip_ticket = 499.99
normal_ticket = 249.99
total = 0

if category == "Normal":
    if 1 <= people_in_the_group <= 4:
        transport = budget * 0.75
        total = (people_in_the_group * normal_ticket) + transport
    elif 5 <= people_in_the_group <= 9:
        transport = budget * 0.60
        total = (people_in_the_group * normal_ticket) + transport
    elif 10 <= people_in_the_group <= 24:
        transport = budget * 0.50
        total = (people_in_the_group * normal_ticket) + transport
    elif 25 <= people_in_the_group <= 49:
        transport = budget * 0.40
        total = (people_in_the_group * normal_ticket) + transport
    else:
        transport = budget * 0.25
        total = (people_in_the_group * normal_ticket) + transport
else:
    if 1 <= people_in_the_group <= 4:
        transport = budget * 0.75
        total = (people_in_the_group * vip_ticket) + transport
    elif 5 <= people_in_the_group <= 9:
        transport = budget * 0.60
        total = (people_in_the_group * vip_ticket) + transport
    elif 10 <= people_in_the_group <= 24:
        transport = budget * 0.50
        total = (people_in_the_group * vip_ticket) + transport
    elif 25 <= people_in_the_group <= 49:
        transport = budget * 0.40
        total = (people_in_the_group * vip_ticket) + transport
    else:
        transport = budget * 0.25
        total = (people_in_the_group * vip_ticket) + transport

diff = abs(budget - total)

if budget >= total:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')

# test input 1000 Normal 1
# test input 30000 VIP 49
