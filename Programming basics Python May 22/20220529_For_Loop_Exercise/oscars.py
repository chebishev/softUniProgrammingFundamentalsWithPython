actor_name = input()
academy_points = float(input())
jury_count = int(input())
total_points = academy_points

for numbers in range(jury_count):
    jury_member = input()
    points = float(input())
    total_points += (len(jury_member) * points) / 2

    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {(1250.5 - total_points):.1f} more!')

# test input Zahari Baharov 205 4 Johnny Depp 45 Will Smith 29 Jet Lee 10 Matthew Mcconaughey 39
# test input Sandra Bullock 340 5 Robert De Niro 50 Julia Roberts 40.5 Daniel Day-Lewis 39.4 Nicolas Cage 29.9 Stoyanka Mutafova 33
