import sys


def print_line_separator_with_title(title, separator, line_length):
    """Function to print separation line with some title inside"""
    try:
        if len(separator) != 1:
            raise Exception("Separator length not equal to 1")
        if len(title) > line_length:
            raise Exception("Title length greater than line_length")
        # Initializing string of separators as a list
        separator_only_str = []
        # Filling empty string with separators only
        for i in range(int(line_length) - len(title)):
            separator_only_str.append(separator)
        # Finding middle position of separator only string
        mid_pos = len(separator_only_str) // 2
        # Extending string as a list by title
        separation_line = separator_only_str[:mid_pos] + [title] + separator_only_str[mid_pos:]
        # Joining string as a list to create regular string
        separation_line = "".join(separation_line)
        # print
        print(separation_line)
    except ValueError as e:
        print("Wrong function input value: " + str(e))
        sys.exit(1)
    except TypeError as e:
        print("Wrong function input type: " + str(e))
        sys.exit(1)
    except Exception as e:
        print("Exception: " + str(e))
        sys.exit(1)
