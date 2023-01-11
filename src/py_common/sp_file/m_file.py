# Imports

import os


def create_new_file(dest_file):
    # Check if destination file folder exists
    if not os.path.exists(os.path.dirname(dest_file)):
        print(f"Destination folder {os.path.dirname(dest_file)} not exist")
        return 11
    # Check if file not yet exist
    if not os.path.exists(dest_file):
        # Create new file
        fp = open(dest_file, "x")
        fp.close()
        print(f"SUCCESS: File {dest_file} created")
        return 0
    else:
        # Skip if file exist
        print(f"SKIP: File {dest_file} already exist")
        return 0


def overwrite_line_with_matching_prefix_to_file(dest_file, prefix, value):
    # Check if destination file exists
    if not os.path.exists(dest_file):
        print(f"Destination file {dest_file} not exist")
        return 10
    # Opening file to append or edit line
    line_found = False
    line_match = False
    output = ""
    replaced_line = ""
    with open(dest_file, "r") as file:
        # Looking for line containing prefix
        for line in file:
            if line.startswith(prefix):
                line_found = True
                if line == prefix + value + "\n":
                    # Skiping as line already added
                    print(f"SKIP: Line {line} already added")
                    line_match = True
                    return 0
                else:
                    # Replacing line with new values
                    replaced_line = line.replace(line, prefix + value) + "\n"
                    print(f"Replacing {line} with {prefix}{value}")
                    print(f"SUCCESS: Line added to file {dest_file}")
                    return 0
            else:
                replaced_line = line
            output = output + replaced_line
    if line_found == True and line_match == False:
        with open(dest_file, "w") as file:
            file.write(output)
    elif line_found == False:
        with open(dest_file, "r+") as file:
            # Move pointer to the end of the file
            file.seek(0, 2)
            # Adding new line at the end
            file.write(f"{prefix}{value}\n")
            print(f"Adding {prefix}{value} as new line")
            print(f"SUCCESS: Line added to file {dest_file}")
            return 0
