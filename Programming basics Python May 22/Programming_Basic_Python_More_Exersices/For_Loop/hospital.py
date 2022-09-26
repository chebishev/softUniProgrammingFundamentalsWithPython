period = int(input())
treated_patients = 0
untreated_patients = 0
available_doctors = 7

for numbers in range(1, period + 1):
    patients_count = int(input())

    if numbers % 3 == 0:
        if untreated_patients > treated_patients:
            available_doctors += 1

    if patients_count > available_doctors:
        untreated_patients += (patients_count - available_doctors)
        treated_patients += available_doctors
    else:
        treated_patients += patients_count

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')

# test input 4 7 27 9 1
# test input 6 25 25 25 25 25 2
# test input 3 7 7 7
