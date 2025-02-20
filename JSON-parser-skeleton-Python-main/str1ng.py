import re
# def parse_string(input_string):
#     """Parses string
#     >>> parse_string('"abc" rest')
#     ("abc", " rest")
#     >>> parse_string("something else")
#     None
#     """

pattern = r'(\\|/|"|[\b]|\f|\n|\r|\t|\uFFFF)'

f = open("positive_string_tests_v2.txt", "r")
content = f.read()
content_list = content.split('\n')
print(content_list[0:99])
wrongly_matched = 0
correctly_matched = 0
for i in range(10000):
    data = re.search(pattern, content_list[i])
    if data is None:
        correctly_matched += 1
        print(f"{data} line no: {i+1} with string : {content_list[i]} is correctly matched")
    else:
        wrongly_matched += 1
        #print(f"line no: {i + 1} with string : {content_list[i]} is wrongly matched")
print(f"There are {correctly_matched} correctly matched test cases")
print(f"There are {wrongly_matched} wrongly matched test cases")
