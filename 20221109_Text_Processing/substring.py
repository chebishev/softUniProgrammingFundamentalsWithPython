piece_of_string = input()
string_to_cut = input()
while piece_of_string in string_to_cut:
    string_to_cut = string_to_cut.replace(piece_of_string, "")
print(string_to_cut)

# test input:

# ice
# kicegiciceeb
