range_start = int(input())
range_end = int(input())

start_one = range_start // 1000
start_two = range_start % 1000 // 100
start_three = range_start % 100 // 10
start_four = range_start % 10

end_one = range_end // 1000
end_two = range_end % 1000 // 100
end_three = range_end % 100 // 10
end_four = range_end % 10

for thousands in range(start_one, end_one + 1):
    for hundreds in range(start_two, end_two + 1):
        for tens in range(start_three, end_three + 1):
            for ones in range(start_four, end_four + 1):
                if thousands % 2 != 0 and \
                        hundreds % 2 != 0 and \
                        tens % 2 != 0 and \
                        ones % 2 != 0:
                    print(f"{thousands}{hundreds}{tens}{ones}", end=" ")
                else:
                    continue
# test input 2345 6789
# test input 3256 6579
# test input 1365 5877
