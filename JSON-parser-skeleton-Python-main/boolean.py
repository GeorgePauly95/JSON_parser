import re
def parse_bool(input_string):
    """Parses boolean

    >>> parse_bool("true rest")
    (True, ' rest')

    >>> parse_bool("something else") is None
    True

    """
    data = input_string.startswith(("true","false"))
    if data:
        if input_string[0] == "t":
            remaining_string = input_string[4:]
            final_output = (True, remaining_string)
            return final_output
        elif input_string[0] == "f":
            remaining_string = input_string[5:]
            final_output = False, remaining_string
            return final_output
    return None
if __name__ == "__main__":
    import doctest
    doctest.testmod()