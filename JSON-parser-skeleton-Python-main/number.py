import re

def parse_number(input_string):
    """
        >>> parse_number("0.7649+33") is None
        True
        >>> parse_number("0.9881")
        (0.9881, '')
        >>> parse_number("0e+1")
        (0.0, '')
        >>> parse_number("1.e03") is None
        True
        >>> parse_number("103380")
        (103380, '')
        >>> parse_number("1070.0")
        (1070.0, '')
        >>> parse_number("107Ee6") is None
        True
        >>> parse_number("10923E+5")
        (1092300000.0, '')
        >>> parse_number("1E53.4190") is None
        True
    """
    scientific_float_pattern = "^[-]?(([1-9]([0-9]+)?[.][0-9]+(e|E)[-+]?[0-9]+)|([1-9][0-9]*(e|E)[-+]?[0-9]+)|(0[.][0-9]+(e|E)[-+]?[0-9]+)|(0(e|E)[-+]?[0-9]+))$"
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
#Testing with >60k cases
print(parse_number("0.7649+33"))
#Preparation for Testing and initialization of Variables
f = open('numbertests.txt', 'r')
content = f.read()
content_list =  list(content.splitlines())
i = 0
failed_test_cases_false_positive = []
failed_test_cases_false_negative = []
passed_test_cases_true_positive = []
passed_test_cases_true_negative = []

#Testing
for x in content_list:
    x_list = x.split("  ")
    if parse_number(x_list[0]) == "None" and x_list[1] == "false":
        passed_test_cases_true_negative.append(x_list[0])
    elif parse_number(x_list[0]) != "None" and  x_list[1] == "false":
        failed_test_cases_false_positive.append(x_list[0])
    elif parse_number(x_list[0]) == "None" and x_list[1] == "true":
        failed_test_cases_false_negative.append(x_list[0])
    elif parse_number(x_list[0]) != "None" and x_list[1] == "true":
        passed_test_cases_true_positive.append(x_list[0])

#Checking the Results
print(f"Total test case count: {len(content_list)}")
print(f"correctly detected numbers: {len(passed_test_cases_true_positive)}, {passed_test_cases_true_positive}")
print(f"correctly detected non numbers: {len(passed_test_cases_true_negative)}, {passed_test_cases_true_negative}")
print(f"wrongly detected non numbers: {len(failed_test_cases_false_negative)}, {failed_test_cases_false_negative}")
print(f"wrongly detected numbers: {len(failed_test_cases_false_positive)}, {failed_test_cases_false_positive}")



