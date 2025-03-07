import re
import json
from ast import parse

#reading test case files
f = open("positive_string_tests.txt", "r")
content = f.read()
content_list = list(content.split('\n'))

#string parser function
def parse_string(input_string):
    # """Parses string
    #
    #     >>> parse_string('"abc" rest')
    #     ('abc', ' rest')
    #
    #     >>> parse_string("something else") is None
    #     True
    #
    # """
    pattern = '^\"([^\"\\\\\x00-\x1f\x7f-\x9f]|(\\\\(b|n|t|\\\\|"|r|f))|(\\\\u[a-fA-F0-9]{4}))*\"'
    data = re.search(pattern,input_string)
    if data is not None:
        output = (data[0])[1:-1]
        if '\\' in output:
            fin_output = output.encode().decode('unicode_escape')
            return fin_output, input_string[len(data[0]):]
        return output, input_string[len(data[0]):]
    return None

# n = len(content_list)

# Testing the function against python's json library
# Initializing correctness tracking variables

# correct_count = 0
# wrong_count = 0
# json_lib_unicode_error_count = 0
# unknown_json_lib_decode_error_count = 0
# backslash_count = 0
# for i in range(n):
#     try:
#         if json.loads(content_list[i]) == parse_string(content_list[i]):
#             correct_count += 1
#             #print("Line no:", i + 1, parse_string(content_list[i]), "equal", json.loads(content_list[i]))
#             continue
#         wrong_count += 1
#         print("Line no:", i+1, parse_string(content_list[i]), "unequal", json.loads(content_list[i]), content_list[i])
#     except json.decoder.JSONDecodeError:
#         print(f"line no. {i+1}: invalid string")
#     except UnicodeEncodeError:
#         print(f"line no. {i+1}: invalid string for the json lib")
#
# print(f"Correct count: {correct_count}")
# print(f"Wrong count: {wrong_count}")
# print(f"Issues with json lib encoding: {json_lib_unicode_error_count}")



# Checking >90K test cases for valid and invalid strings each.

# count_none = 0 # should be 0 for the entire positive string test case
# count_non_none = 0 # should be 0 for the entire negative string test case
# unicode_error_count = 0
# for i in range(n):
#     try:
#         if parse_string(content_list[i]) is None:
#             count_none += 1
#             #print("line no.", i+1, "detected correct", content_list[i])# (for negative test case)
#             print("line no." ,i+1, "is detected wrong", parse_string(content_list[i]), content_list[i])# (for positive test case)
#         else:
#             count_non_none +=1
#             #print(f"line no.", i+1, "detected wrong", parse_string(content_list[i]))# (for negative test case)
#             print("line no." ,i+1, "is detected correct", parse_string(content_list[i]))# (for positive test case)
#     except UnicodeEncodeError:
#         print("unicode error on line no:", i+1)
#         unicode_error_count += 1

# print(f"None Counts: {count_none}")
# print(f"Non None Counts: {count_non_none}")
# print(unicode_error_count)