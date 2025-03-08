def parse_null(input_string):
    """Parses null
    >>> parse_null("null rest")
    (None, ' rest')
    >>> parse_null("something else") is None
    True
    """
    data = input_string.startswith("null")
    if not data:
        return None
    remaining_string = input_string[4:]
    final_output = (None, remaining_string)
    return final_output