budget_for_actors = float(input())
temp_budget = budget_for_actors
command = input()
while command != "ACTION":
    actor_name = command
    if len(actor_name) <= 15:
        temp_budget -= float(input())
    else:
        temp_budget -= temp_budget * 0.20
    if temp_budget <= 0:
        print(f"We need {abs(temp_budget):.2f} leva for our actors.")
        break
    command = input()
    if command == "ACTION":
        print(f"We are left with {temp_budget:.2f} leva.")
        break

# test inputs

# 90000
# Christian Bale
# 70000.50
# Leonard DiCaprio
# Kevin Spacey
# 24000.99

# 170000
# Ben Affleck
# 40000.50
# Zahari Baharav
# 80000
# Tom Hanks
# 2000.99
# ACTION