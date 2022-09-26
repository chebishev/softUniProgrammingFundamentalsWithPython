needed_money = int(input())
command = input()
total_money = 0
credit_card_sum = 0
cash_sum = 0
success_cc = 0
success_cs = 0

while command != "End":
    if total_money >= needed_money:
        average_cc = credit_card_sum / success_cc
        average_cs = cash_sum / success_cs
        print(f"Average CS: {average_cs:.2f}")
        print(f"Average CC: {average_cc:.2f}")
        break
    transaction_even_odd = 1
    while total_money < needed_money:
        price = int(command)
        if transaction_even_odd % 2 == 0:
            if price < 10:
                print("Error in transaction!")
            else:
                credit_card_sum += price
                total_money += price
                success_cc += 1
                print("Product sold!")
        else:
            if price > 100:
                print("Error in transaction!")
            else:
                cash_sum += price
                total_money += price
                success_cs += 1
                print("Product sold!")
        if total_money >= needed_money:
            break
        command = input()
        if command == "End":
            print("Failed to collect required money for charity.")
            break
        transaction_even_odd += 1

# test input 500 120 8 63 256 78 317
# test input 600 86 150 98 227 End
