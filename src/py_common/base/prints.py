"""
Custom print functions to print predefined schemas
"""


# Imports

# Function definitions
def print_line_separator_with_title(title, separator, line_length):
    """Function to print separation line with some title inside

    Raises:
        Exception: "Separator length not equal to 1" when spearator is longer than one sign
        Exception: "Title length greater than line_length" when text to be added is longer than separator it self

    Returns:
        int: Error codes where 0 if sucedded
    """
    if len(separator) != 1:
        raise Exception("Separator length not equal to 1")
    if len(title) > line_length:
        raise Exception("Title length greater than line_length")
    # Initializing string of separators as a list
    separator_only_str = []
    # Filling empty string with separators only
    for _ in range(int(line_length) - len(title)):
        separator_only_str.append(separator)
    # Finding middle position of separator only string
    mid_pos = len(separator_only_str) // 2
    # Extending string as a list by title
    separation_line = separator_only_str[:mid_pos] + [title] + separator_only_str[mid_pos:]
    # Joining string as a list to create regular string
    separation_line = "".join(separation_line)
    # print
    print(separation_line)
    return 0
