import re

number_of_inputs = int(input())
pattern = r'([A-Z][a-z]{2,}\s[A-Z][a-z]{2,})[#]+(([A-Za-z]+)([&]{1}([A-z]+))?([&]{1}([A-z]+))?)[\d]{2}(([A-Za-z0-9]+)\s(Ltd\.|JSC))'
for index in range(number_of_inputs):
    current_employee = input()
    result = re.split(pattern, current_employee)
    if len(result) > 1:
        employee_name = result[1]
        job_position = result[2]
        if "&" in job_position:
            job_position = job_position.replace("&", " ")
        company_name = result[8]
        print(f"{employee_name} is {job_position} at {company_name}")

# test inputs:

# 4
# Tanya Petrova##Dental&Assistants25Health Ltd.
# Kalina Mihova#Occupational&Therapy&Aides00Health Ltd.
# George Fill####Orderlies99Health JSC
# Lily petrova#Speech&Pathology&Assistants60Health Ltd.

# 4
# Peter PetrovPsychology&Teachers25School Ltd.
# Kalin kalinov#Special Education Teachers00 School Ltd.
# Lilyana Kuncheva#### Tutor999School JSC
# Kliment Genchev#Teacher&Assistants20School Ltd.

# 2
# Mariya Ivanova#Photographer&&Machine25PhotoStudio12 Ltd.
# Monica Hristova####Nuclear&Engineer99Station JSC
