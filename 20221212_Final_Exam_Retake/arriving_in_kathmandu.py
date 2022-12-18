import re

pattern = r"([A-Za-z0-9?@#!$]+)=(\d+)<<(.+)"

while True:

    message = input()
    if message == "Last note":
        break

    # tuple in a list. Index 0 - peak name, index 1 - length of geohashcode, index 2 - geohashcode
    search_pattern = re.split(pattern, message)
    if len(search_pattern) == 5:
        hidden_peak_name = search_pattern[1]
        length = int(search_pattern[2])
        geohashcode = search_pattern[3]
        if len(geohashcode) == length:
            peak_name = ""
            for symbol in hidden_peak_name:
                if symbol == "!" or symbol == "@" or symbol == "#" or symbol == "$" or symbol == "?":
                    continue
                else:
                    peak_name += symbol
            if peak_name:
                print(f"Coordinates found! {peak_name} -> {geohashcode}")
            else:
                print("Nothing found!")
        else:
            print("Nothing found!")
    else:
        print("Nothing found!")

# test inputs:

# !@Ma?na?sl!u@=7<<tv58ycb4845
# E!ve?rest=.6<<tuvz26
# !K@2.,##$=4<<tvnd
# !Shiha@pan@gma##9<<tgfgegu67
# !###Anna@pur@na##=16<<tv5dekdz8x11ddkc
# Last note

# Ka?!#nch@@en@ju##nga@=3<<thfbghvn
# =9Cho?@#Oyu<<thvb7ydht
# Nan??ga#Par!ba!t?=16<<twm03q2rx5hpmyr6
# Dhau??la#gi@ri?!#=3<<bvnfhrtiuy
# Last note
