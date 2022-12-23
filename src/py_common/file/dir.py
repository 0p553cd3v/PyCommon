"""
Standard operations on paths
"""

# Imports
import os

# Functions
def create_dir(path):
    """Standard mkdir extended fith exception handling"""
    # Check if folder exists
    if not os.path.exists(path):
        try:
            # Creating dir if not existing
            os.makedirs(path)
        except PermissionError as e:
            # logger.exception(f"Permission denied during directory creation: {path}")
            print(f"Permission denied during directory creation: {path}")
            raise PermissionError(f"Permission denied during directory creation: {path}")
        else:
            # logger.info(f"SUCCESS: Directory {path} succesfully created")
            print(f"SUCCESS: Directory {path} succesfully created")
            return True
    else:
        # Skipp if folder exist
        # logger.info(f"SKIP: Direcotry already exist: {path}")
        print(f"SKIP: Path already exist: {path}")
        return True

