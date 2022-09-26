tabs = int(input())
salary = float(input())

for numbers in range(tabs):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(f'{salary:.0f}')

# test input 10 750 Facebook Dev.bg Instagram Facebook Reddit Facebook Facebook
# test input 3 500 Github.com Stackoverflow.com softuni.bg
