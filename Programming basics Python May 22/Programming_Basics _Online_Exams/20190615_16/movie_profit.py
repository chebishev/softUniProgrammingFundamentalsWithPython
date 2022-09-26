movie_name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_percent = int(input()) / 100
total = (tickets * ticket_price * days)
total -= total * cinema_percent
print(f"The profit from the movie {movie_name} is {total:.2f} lv.")

# test input The Programmer 20 500 7.50 7
# test input Python Basics 40 34785 10.45 14
# test input The Jungle 22 20500 9.37 30
