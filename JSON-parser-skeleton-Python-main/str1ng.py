import re
def parse_string(input_string):
    """Parses string
    >>> parse_string('"abc" rest')
    ("abc", " rest")
    >>> parse_string("something else")
    None
    """
