from null import parse_null
from boolean import parse_bool
from number import parse_number
from str1ng import parse_string
from array import parse_array

def parse_object(input_string):
    '''
    >>> parse_object('{, "a " :false ,"b": 2e2, "c": false }') is None
    True
    >>> parse_object('{ "a" :false ,,"b": 2e2, "c": false }') is None
    True
    >>> parse_object('{ "a" :false ,"b": 2e2, "c": false, }') is None
    True
    >>> parse_object('{ "a" :false ,"b": renk, "c": false, }') is None
    True
    >>> parse_object('{ "name" : "John" ,"age" : {"a":30,"b":32,"c":{"70":[1e0,2E0,5,12,35,7e1]},"d":63} ,"city" : {"a":1,"b":2,"c":3},"country":null,"eye":false,"ear":true, "s":true} rest')
    ({'name': 'John', 'age': {'a': 30, 'b': 32, 'c': {'70': [1.0, 2.0, 5, 12, 35, 70.0]}, 'd': 63}, 'city': {'a': 1, 'b': 2, 'c': 3}, 'country': None, 'eye': False, 'ear': True, 's': True}, ' rest')
    '''
    if input_string[0] != "{" or input_string[0:2] == "{,":
        return None
    input_string = input_string[1:]
    output_object = {}
    while input_string[0] != "}":
        input_string = input_string.lstrip(" ") # No.1 Whitespace before the key
        key_string = parse_string(input_string)
        if key_string is None:
            return None
        parsed_key = key_string[0]
        input_string = key_string[1]
        input_string = input_string.lstrip(" ") # No.2 Whitespace after the key and before the colon
        if input_string[0] != ":":
            return None
        else:
            if input_string[1] == ":" or input_string[1] == "," or input_string[1] == "}": # not sure if colon is required as a case here
                return None
            input_string = input_string[1:]
        input_string = input_string.lstrip(" ") # No. 3 Whitespace after the colon and before the value
        if parse_null(input_string) is not None:
            parsed_null = parse_null(input_string)
            output_object[parsed_key] = parsed_null[0]
            input_string = parsed_null[1]
        elif parse_bool(input_string) is not None:
            parsed_bool = parse_bool(input_string)
            output_object[parsed_key] = parsed_bool[0]
            input_string = parsed_bool[1]
        elif parse_number(input_string) is not None:
            parsed_number = parse_number(input_string)
            output_object[parsed_key] = parsed_number[0]
            input_string = parsed_number[1]
        elif parse_string(input_string) is not None:
            parsed_string = parse_string(input_string)
            output_object[parsed_key] = parsed_string[0]
            input_string = parsed_string[1]
        elif parse_array(input_string) is not None:
            parsed_array = parse_array(input_string)
            output_object[parsed_key] = parsed_array[0]
            input_string = parsed_array[1]
        elif parse_object(input_string) is not None:
            parsed_object = parse_object(input_string)
            output_object[parsed_key] = parsed_object[0]
            input_string = parsed_object[1]
        input_string = input_string.lstrip(" ") # No.4 Whitespace after the value and before the comma
        if input_string[0] == ",":
            if input_string[1] == "," or input_string[1] == "}":
                return None
            input_string = input_string[1:]
            continue
        elif input_string[0] == "}":
            break
        return None
    return output_object, input_string[1:]