last_sector = ord(input()) # B
first_sector_rows = int(input()) # 3
odd_row_seats = int(input()) # 2
last_sector_rows = (last_sector - 65) + first_sector_rows # 4
sector_count = 0
row_count = 0
even_seats = odd_row_seats + 2
for sectors in range(65, last_sector+1):
    while True:
        sector_rows = first_sector_rows
        for rows in range(1, first_sector_rows+1):
            temp_seat = 97
            if rows % 2 == 0:
                for seats_even in range(2, even_seats+1):
                    print(f'{chr(sectors)}{rows}{chr(temp_seat)}')
                    temp_seat += 1
                    even_seats += 1
            else:
                for seats_odd in range(1, odd_row_seats + 1):
                    print(f'{chr(sectors)}{rows}{chr(temp_seat)}')
                    temp_seat += 1
                    odd_row_seats += 1
            if last_sector_rows == rows:
                temp_seat = 97
                break
        sector_rows += 1


print(last_sector)
# A = 65
# Z = 90
# a = 97
# z = 122

# test input B 3 2
