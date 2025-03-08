from null import parse_null
from boolean import parse_bool
from number import parse_number
from str1ng import parse_string
from array import parse_array
from object import parse_object

def parse_json(input_string):
    # """Parses json
    # >>> parse_json('[{"my": "value"}, 2, "just string"]')
    # [{"my": "value"}, 2, "just string"]
    # >>> parse_json('[{"my": "value"}, 2, "just string"] fakjds;')
    # Traceback (most recent call last):
    #     ...
    # ValueError: Extra data
    # >>> parse_json('true')
    # True
    # """
    parsers = [parse_null,parse_bool,parse_number,parse_string,parse_array,parse_object]
    for parser in parsers:
        result = parser(input_string)
        if result:
            if result[1] == "":
                return result[0]
            return None
    return None
print(parse_json('[[[ [1,2,3,4,5], true, null ,23e-2]],"george", false , 2E2, [1.5,2,true,1234567,[1,2,3,4,5]]]'))