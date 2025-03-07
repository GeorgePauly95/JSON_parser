from boolean import parse_bool
from null import parse_null
from number import parse_number
from str1ng import parse_string

def first_character_checker(character,input_string):
    if input_string[0] == character:
        input_string = input_string[1:]
        if input_string[0] == character:
            return None
        return input_string
    return input_string

def parse_array(input_string):
    if input_string[0] != "[":
        return None
    input_string = input_string[1:]
    output_array = []
    while input_string[0] != "]":
        input_string = first_character_checker(",",input_string)
        if input_string is None:
            return None
        input_string = input_string.lstrip(" ")
        parsed_null = parse_null(input_string)
        parsed_bool = parse_bool(input_string)
        parsed_number = parse_number(input_string)
        parsed_string = parse_string(input_string)

        if parsed_null is not None:
            output_array.append(parsed_null[0])
            input_string = parsed_null[1]
        if parsed_bool is not None:
            output_array.append(parsed_bool[0])
            input_string = parsed_bool[1]
        if parsed_number is not None:
            output_array.append(parsed_number[0])
            input_string = parsed_number[1]
        if parsed_string is not None:
            output_array.append(parsed_string[0])
            input_string = parsed_string[1]

        input_string = input_string.lstrip(" ")

        if input_string[0] == ",":
            continue
        elif input_string[0] == "]":
            break
        elif input_string[0] == "[":
            parsed_array = parse_array(input_string)
            if  parsed_array is not None:
                output_array.append(parsed_array[0])
                input_string = parsed_array[1]
            else:
                return None
        else:
            return None
    return output_array, input_string[1:]

str_1 = '[[[ [1,2,3,4,5], true , null , 23e-2 ]], "george" , 2E2 , [1, 2 ,true, 1234567,[1,2,3,4,5]]] rest'
str_2 = '[[1,2,3,4],true,false,null , "pauly" ] rest'
str_3 = '[  true  , false] ["rest"]'
str_4 = '[ ] rest'
str_5 = '[true,[false],12] rest'
str_6 ='[[],[]] rest'

