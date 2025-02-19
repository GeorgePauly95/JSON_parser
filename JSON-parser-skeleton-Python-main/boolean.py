import re

def parse_bool(input_string):
    """Parses boolean

    >>> parse_bool("true rest")
    (True, ' rest')

    >>> parse_bool("something else")
    None

    """
    data = input_string.startswith(("true","false"))
    if data:
        if input_string[0] == "t":
            remaining_string = input_string[4:]
            final_output = (True, remaining_string)
            return final_output
        elif input_string[0] == "f":
            remaining_string = input_string[5:]
            final_output = (False, remaining_string)
    else:
        return None
    # data = re.search('true|false',input_string)
    # if data is not None:
    #     if data[0] == 'true':
    #         output = input_string.replace('true','')
    #         final_output = (True, output)
    #         return final_output
    #     elif data[0] == 'false':
    #         output = input_string.replace('false', '')
    #         final_output = (False, output)
    #         return final_output
    # else:
    #     print(None)



if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(parse_bool("false yolo"))