import re

def parse_number(input_string):
    scientific_float_pattern = "^[-]?(([1-9][0-9]+[.][0-9]+(e|E)[-+]?[1-9][0-9]*)|([1-9][0-9]*(e|E)[-+]?[1-9][0-9]*)|(0[.][0-9]+(e|E)[-+]?[1-9][0-9]*)|(0(e|E)[-+]?[0-9]+))$"
    data = re.search(scientific_float_pattern,input_string)
    if data is not None:
        remaining_string = input_string[len(data[0]):]
        final_output = (float(data[0]),remaining_string)
        return final_output
    else:
        float_pattern = "^[-]?([1-9][0-9]*[.][0-9]+|0[.][0-9]+)$"
        data = re.search(float_pattern, input_string)
        if data is not None:
            remaining_string = input_string[len(data[0]):]
            final_output = (float(data[0]), remaining_string)
            return final_output
        else:
            integer_pattern = "^[-]?([1-9][0-9]*|0)$"
            data = re.search(integer_pattern,input_string)

            if data is not None:
                remaining_string = input_string[len(data[0]):]
                final_output = (int(data[0]), remaining_string)
                return final_output
            else:
                return "None"