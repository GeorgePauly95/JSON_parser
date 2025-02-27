import re
#reading test case files
f = open("positive_string_tests.txt", "r")
content = f.read()
content_list = list(content.split('\n'))
pattern  = '^"([^"(\\\\)\x00\x01\x08\x09\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f]*|(\\\\b)*|(\\\\n)|(\\\\t)*|(\\\\\\\\)*|(\\\")*|(\\\\/)*|(\\\\r)*|(\\\\f)*|(\\\\u[a-fA-F0-9]{4})*)"$'
print(content_list[1510])

#string parser function
def string_parser(input_string):
    data = re.search(pattern,input_string)
    if data is not None:
        return data[0]
    return None

#Testing the function
print(string_parser(content_list[1510]))

#Checking >90K test cases for valid and invalid strings each.
count_none = 0 # should be 0 for the entire positive string test case
count_non_none = 0 # should be 0 for the entire negative string test case
n = len(content_list)
for i in range(n):
    if string_parser(content_list[i]) is None:
        count_none += 1
        # (for negative test case) print(f"line no. {i+1} is detected correct: {content_list[i]}")
        #print(f"line no. {i+1} is detected wrong: {string_parser(content_list[i])}, {content_list[i]}") # (for positive test case)
    else:
        count_non_none +=1
        # (for negative test case) print(f"line no. {i+1} is detected wrong,: {string_parser(content_list[i])}")
        #print(f"line no. {i+1} is detected correct (but maybe parsed wrong): {string_parser(content_list[i])}") # (for positive test case)



print(f"None Counts: {count_none}")
print(f"Non None Counts: {count_non_none}")