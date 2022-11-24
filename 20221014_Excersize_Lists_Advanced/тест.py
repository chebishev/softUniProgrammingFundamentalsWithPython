def fire(opponent, index, damage):
    if 0 <= index < len(opponent):
        opponent[index] -= damage
    return opponent


def defend(pirate, index, end_index, damage):
    # Коментар за тази променлива съм писал под командата Defend
    valid = 0 <= index < len(pirate) and index < end_index < len(pirate)
    if valid:
        for i in range(len(pirate)):
            # това е проверка за валиден индекс под проверка за валиден индекс...
            # Щом е подчертано значи има по-добър начин, но в случая няма смисъл
            if i >= index and i <= end_index:
                pirate[i] -= damage

    return pirate


def repair(pirate, index, health, max_health):
    if 0 <= index < len(pirate):
        pirate[index] += health
        if pirate[index] >= max_health:
            pirate[index] = max_health
    return pirate


def status(pirate, max_health):
    sections = 0
    health = max_health * 0.20
    for i in pirate:
        if i < health:
            sections += 1

    print(f'{sections} sections need repair.')


pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
health_capacity = int(input())
legal = False

while True:
    command = input()
    if command == 'Retire':
        break

    to_do = command.split()
    action = to_do[0]
    if len(to_do) > 1:
        if len(to_do) > 3:
            first_value = int(to_do[1])
            second_value = int(to_do[2])
            third_value = int(to_do[3])

        else:
            first_value = int(to_do[1])
            second_value = int(to_do[2])

    if action == 'Fire':
        if 0 <= first_value < len(warship):
            warship = fire(warship, first_value, second_value)
            if warship[first_value] <= 0:
                print('You won! The enemy ship has sunken.')
                legal = True
                break
    elif action == 'Defend':
        # Това valid е доста сложно и под него имаш IF.
        # по-добре да си спестиш променливата и да е направо:
        # if 0 <= first_value < len(pirate_ship) and second_value < len(pirate_ship):
        # не е нужно second value да е по-голямо от first_value
        # Същата проверка я имаш и във функцията, което я обезмисля на едно от двете места и
        # и тъй като не успях да го оправя така че да работи с фунцкията, я махнах :)
        valid = 0 <= first_value < len(pirate_ship) and first_value < second_value < len(pirate_ship)
        if valid:
            pirate_ship = defend(pirate_ship, first_value, second_value, third_value)
            for i in pirate_ship:
                if i <= 0:
                    print('You lost! The pirate ship has sunken.')
                    legal = True
                    break
    elif action == 'Repair':
        pirate_ship = repair(pirate_ship, first_value, second_value, health_capacity)

    elif action == 'Status':
        status(pirate_ship, health_capacity)

pirate_ship_status = 0   # sum(pirate_ship_status)
warship_status = 0       # sum(warship_status)
# двата фор цикъла можеш да ги избегнещ. Функцията sum сумира
# елементите в list oт интиджъри
for i in pirate_ship:
    pirate_ship_status += i

for b in warship:
    warship_status += b

if legal == False: # Това неслучайно го подчертава. Можеш да го замениш с if not legal
    print(f'Pirate ship status: {pirate_ship_status}')
    print(f'Warship status: {warship_status}')

