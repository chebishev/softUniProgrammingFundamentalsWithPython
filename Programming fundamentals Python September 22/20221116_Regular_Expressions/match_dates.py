import re

dates = input()
search_match = r"\b(\d{2})([.\/-])([A-Z][a-z]{2})(\2)(\d{4})\b"
result = re.findall(search_match, dates)
for element in result:
    print(f"Day: {element[0]}, Month: {element[2]}, Year: {element[4]}")

# test input:

# 13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
