from null import parse_null
from boolean import parse_bool
from number import parse_number
from str1ng import parse_string



def parse_array(input_string):
    '''
    >>> parse_array('[,1,2,3,4,5] rest') is None
    True
    >>> parse_array('[1,,,2,3,4,5] rest') is None
    True
    >>> parse_array('[1,2,3,4,5,] rest') is None
    True
    >>> parse_array('[1,2,3,4,5,bbb] rest') is None
    True
    >>> parse_array('[[[ [1,2,3,4,5], true, null ,23e-2]],"george", false , 2E2, [1.5,2,true,1234567,[1,2,3,4,5]]] rest')
    ([[[[1, 2, 3, 4, 5], True, None, 0.23]], 'george', False, 200.0, [1.5, 2, True, 1234567, [1, 2, 3, 4, 5]]], ' rest')
    '''
    from object import parse_object
    if input_string[0] != "[" or input_string[0:2] == "[,":
        return None
    input_string = input_string[1:]
    output_array = []

    while input_string[0] != "]":
        input_string = input_string.lstrip(" ")

        # if parse_null(input_string) is not None:
        #     parsed_null = parse_null(input_string)
        #     output_array.append(parsed_null[0])
        #     input_string = parsed_null[1]
        # elif parse_bool(input_string) is not None:
        #     parsed_bool = parse_bool(input_string)
        #     output_array.append(parsed_bool[0])
        #     input_string = parsed_bool[1]
        # elif parse_number(input_string) is not None:
        #     parsed_number = parse_number(input_string)
        #     output_array.append(parsed_number[0])
        #     input_string = parsed_number[1]
        # elif parse_string(input_string) is not None:
        #     parsed_string = parse_string(input_string)
        #     output_array.append(parsed_string[0])
        #     input_string = parsed_string[1]
        # elif parse_array(input_string) is not None:
        #     parsed_array = parse_array(input_string)
        #     output_array.append(parsed_array[0])
        #     input_string = parsed_array[1]
        # elif parse_object(input_string) is not None:
        #     parsed_object = parse_object(input_string)
        #     output_array.append(parsed_object[0])
        #     input_string = parsed_object[1]

        input_string = input_string.lstrip(" ")
        if input_string[0] == ",":
            if input_string[1] == "," or input_string[1] == "]":
                return None
            input_string = input_string[1:]
            continue
        elif input_string[0] == "]":
            break
        return None
    return output_array, input_string[1:]
print(parse_array('[[[ [1,2,3,4,5], true, null ,23e-2]],"george", false , 2E2, [1.5,2,true,1234567,[1,2,3,4,5]]] rest'))