import textwrap

string_with_no_equal_words = "колкомногодуми с петбуквиможемлесночесточистоизчетем"

if len(string_with_no_equal_words) / 5 == len(string_with_no_equal_words) // 5:
    test_list = textwrap.wrap(string_with_no_equal_words, 5)
else:
    test_list = textwrap.wrap(string_with_no_equal_words, 5)
    test_list[-2] = test_list[-2] + test_list[-1]
    test_list.pop()

print(test_list)