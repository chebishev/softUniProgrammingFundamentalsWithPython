budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = gpu_count * 250
cpu_price = (gpu_price * 0.35) * cpu_count
ram_price = (gpu_price * 0.10) * ram_count

total_sum = gpu_price + cpu_price + ram_price

if gpu_count > cpu_count:
    total_sum *= 0.85

if total_sum <= budget:
    print(f"You have {(budget - total_sum):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total_sum - budget):.2f} leva more!")

# test input 900 2 1 3
# test input 920.45 3 1 1
