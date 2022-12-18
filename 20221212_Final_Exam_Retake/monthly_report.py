monthly_report_dict = {"distributors": {}, "clients": {}}
total_income = 0
while True:
    command = input()
    if command == "End":
        break

    action, name, money = command.split()
    money = float(money)
    if action == "Deliver":
        if name not in monthly_report_dict["distributors"].keys():
            monthly_report_dict["distributors"][name] = 0
        monthly_report_dict["distributors"][name] += money
    elif action == "Return":
        if name in monthly_report_dict["distributors"].keys():
            if money > monthly_report_dict["distributors"][name]:
                continue
            monthly_report_dict["distributors"][name] -= money
            if monthly_report_dict["distributors"][name] == 0:
                del monthly_report_dict["distributors"][name]
    elif action == "Sell":
        if name not in monthly_report_dict["clients"].keys():
            monthly_report_dict["clients"][name] = 0
        monthly_report_dict["clients"][name] += money
        total_income += money

for client, amount in monthly_report_dict["clients"].items():
    print(f"{client}: {amount:.2f}")
print("-----------")
for distributor, amount in monthly_report_dict["distributors"].items():
    print(f"{distributor}: {amount:.2f}")
print("-----------")
print(f"Total Income: {total_income:.2f}")

# test inputs:

# Deliver Micro 10000.00
# Sell Nick 500.00
# Sell Antony 260.50
# Deliver Micro 2000.50
# End

# Deliver North 200.30
# Sell Peter 30.20
# Return Macro 5000.00
# Return North 100.30
# Sell Peter 50.50
# End

# Deliver North 200.30
# Deliver Micro 10000.00
# Deliver North 150.50
# End
