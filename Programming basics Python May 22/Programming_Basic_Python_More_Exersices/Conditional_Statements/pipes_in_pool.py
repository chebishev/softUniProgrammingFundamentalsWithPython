volume_in_litters = int(input())
pipe_1_per_hour = int(input())
pipe_2_per_hour = int(input())
working_hours = float(input())

pipe_1_total = pipe_1_per_hour * working_hours
pipe_2_total = pipe_2_per_hour * working_hours
litters_total = pipe_1_total + pipe_2_total

if (pipe_1_total + pipe_2_total) <= volume_in_litters:
    total_percent = ((pipe_1_total + pipe_2_total) / volume_in_litters) * 100
    pipe_1_percent = (pipe_1_total / litters_total) * 100
    pipe_2_percent = (pipe_2_total / litters_total) * 100
    print(f"The pool is {total_percent:.2f}% full. Pipe 1: {pipe_1_percent:.2f}%. Pipe 2: {pipe_2_percent:.2f}%.")
else:
    print(f"For {working_hours:.2f} hours the pool overflows with {(pipe_1_total + pipe_2_total - volume_in_litters):.2f} liters.")

# test input 1000 100 120 3
# test input 100 100 100 2.5
