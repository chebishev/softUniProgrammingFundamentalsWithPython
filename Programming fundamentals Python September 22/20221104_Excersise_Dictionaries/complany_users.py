companies_dictionary = {}

while True:

    command = input()
    if command == "End":
        break

    company_name, employee_id = command.split(" -> ")
    if company_name not in companies_dictionary.keys():
        companies_dictionary[company_name] = []
    if employee_id in companies_dictionary[company_name]:
        continue
    companies_dictionary[company_name].append(employee_id)
for key, values in companies_dictionary.items():
    print(key)
    for index in range(len(values)):
        print(f"-- {values[index]}")

# test inputs:

# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End

# SoftUni -> AA12345
# SoftUni -> CC12344
# Lenovo -> XX23456
# SoftUni -> AA12345
# Movement -> DD11111
# End
