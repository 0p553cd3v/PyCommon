"""File operations module."""

# Imports
import os
import shutil


def create_new_file(dest_file_path):
    """Create new file or skip if exist.

    Returns:
        int: Error number
    """
    # Check if destination file folder exists
    if not os.path.exists(os.path.dirname(dest_file_path)):
        print(f"Destination folder {os.path.dirname(dest_file_path)} not exist")
        return 11
    # Check if file not yet exist
    if not os.path.exists(dest_file_path):
        # Create new file
        with open(dest_file_path, "x"):
            pass
        print(f"SUCCESS: File {dest_file_path} created")
        return 0
    else:
        # Skip if file exist
        print(f"SKIP: File {dest_file_path} already exist")
        return 0


def overwrite_line_with_matching_prefix_to_file(dest_file_path: str, prefix: str, value: str):
    """Overwrite line with matching prefix, skip or add if not exist in file.

    Args:
        dest_file_path (str): Path to destination file
        prefix (str): Prefix to be found
        value (str): Value to be added after prefix

    Returns:
        int: Error number
    """
    # Check if destination file exists
    if not os.path.exists(dest_file_path):
        print(f"Destination file {dest_file_path} not exist")
        return 10
    # Opening file to append or edit line
    line_found = False
    new_line = prefix + value + "\n"
    old_line = ""
    matching_line_index = -1
    with open(dest_file_path, "r") as file:
        data = file.readlines()
        for x, _ in enumerate(data):
            if data[x].startswith(prefix):
                line_found = True
                matching_line_index = x
                old_line = data[x]

    if line_found is True:
        if old_line == new_line:
            # Skiping as line already added
            print(f"SKIP: Line {new_line} already added")
            return 0
        else:
            with open(dest_file_path, "r") as file:
                # Looking for line containing prefix
                data = file.readlines()
            data[matching_line_index] = new_line
            with open(dest_file_path, "w") as file:
                file.writelines(data)
            print(f"Replacing {old_line} with {new_line}")
            print(f"SUCCESS: Line added to file {dest_file_path}")
            return 0
    else:
        with open(dest_file_path, "r+") as file:
            # Move pointer to the end of the file
            file.seek(0, 2)
            # Adding new line at the end
            file.write(new_line)
            print(f"Adding {new_line} as new line")
            print(f"SUCCESS: Line added to file {dest_file_path}")
            return 0


def copy_new_file_to_dir(source_file, dest_dir):
    """Copy file if not exist in destination directory.

    Args:
        source_file (path): Path to source file
        dest_dir (path): Desination folder path

    Returns:
        int: Error number
    """
    # Check if destination folder exists
    if not os.path.exists(dest_dir):
        print(f"Folder {dest_dir} not exist")
        return 1
    # Check if source file exists
    if not os.path.exists(source_file):
        print(f"File {source_file} not exist")
        return 2
    # Check if file exists in destination directory
    if not os.path.exists(os.path.join(dest_dir, os.path.basename(source_file))):
        # Copy file to directory if it was not existing
        shutil.copyfile(source_file, os.path.join(dest_dir, os.path.basename(source_file)))
        print(f"SUCCESS: File {source_file} added to directory {dest_dir}")
        return 0
    else:
        # Skip if file exists in destination directory
        print(f"SKIP: File {source_file} already exist in directory {dest_dir}")
        return 0
