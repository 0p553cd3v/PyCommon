"""
Standard operations on paths
"""

# Imports
import os
import shutil

# Functions
def create_dir_if_not_exist(path):
    """Standard mkdir extended fith exception handling"""
    # Check if folder exists
    if not os.path.exists(path):
        try:
            # Creating dir if not existing
            os.makedirs(path)
        except PermissionError as e:
            # logger.exception(f"Permission denied during directory creation: {path}")
            print(f"Permission denied during directory creation: {path}")
            raise PermissionError from e
        else:
            # logger.info(f"SUCCESS: Directory {path} succesfully created")
            print(f"SUCCESS: Directory {path} succesfully created")
            return True
    else:
        # Skipp if folder exist
        # logger.info(f"SKIP: Direcotry already exist: {path}")
        print(f"SKIP: Path already exist: {path}")
        return True


def clean_up_folder_starting_with(directory, prefix):
    """Function to recursively clean a folder on a direcotry which name starts with prefix"""
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if item.startswith(prefix):
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(os.path.join(directory, item)):
                shutil.rmtree(path)
            else:
                raise Exception("No folder prefix match")
    return True
