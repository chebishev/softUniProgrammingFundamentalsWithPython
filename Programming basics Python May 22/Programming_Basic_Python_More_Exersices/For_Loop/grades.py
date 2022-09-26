students = int(input())
grades_total = 0
top_count = 0
good_count = 0
average_count = 0
fail_count = 0

for numbers in range(students):
    grade = float(input())
    grades_total += grade
    if grade < 3.00:
        fail_count += 1
    elif grade < 4.00:
        average_count += 1
    elif grade < 5.00:
        good_count += 1
    else:
        top_count += 1

top_percent = top_count / students * 100
good_percent = good_count / students * 100
average_percent = average_count / students * 100
fail_percent = fail_count / students * 100
average_grade = grades_total / students

print(f'Top students: {top_percent:.2f}%')
print(f'Between 4.00 and 4.99: {good_percent:.2f}%')
print(f'Between 3.00 and 3.99: {average_percent:.2f}%')
print(f'Fail: {fail_percent:.2f}%')
print(f'Average: {average_grade:.2f}')

# test input 10 3.00 2.99 5.68 3.01 4 4 6.00 4.50 2.44 5
# test input 6 2 3 4 5 6 2.2
