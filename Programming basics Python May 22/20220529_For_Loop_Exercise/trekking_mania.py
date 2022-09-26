trekking_groups_count = int(input())
musala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
total_people = 0

for numbers in range(trekking_groups_count):
    group_members_count = int(input())
    total_people += group_members_count
    if group_members_count <= 5:
        musala_count += group_members_count
    elif group_members_count <= 12:
        montblanc_count += group_members_count
    elif group_members_count <= 25:
        kilimanjaro_count += group_members_count
    elif group_members_count <= 40:
        k2_count += group_members_count
    else:
        everest_count += group_members_count

musala_percent = (musala_count / total_people) * 100
montblanc_percent = (montblanc_count / total_people) * 100
kilimanjaro_percent = (kilimanjaro_count / total_people) * 100
k2_percent = (k2_count / total_people) * 100
evereset_percent = (everest_count / total_people) * 100

print(f'{musala_percent:.2f}%')
print(f'{montblanc_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{evereset_percent:.2f}%')

# test input 10 10 5 1 100 12 26 17 37 40 78
# test input 5 25 41 31 250 6
