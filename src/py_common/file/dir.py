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
            return e
        except Exception as e:
            # logger.exception(f"ERROR: {e}")
            print(f"ERROR: {e}")
            return e
        else:
            # logger.info(f"SUCCESS: Directory {path} succesfully created")
            print(f"SUCCESS: Directory {path} succesfully created")
            return 0
    else:
        # Skipp if folder exist
        # logger.info(f"SKIP: Path already exist: {path}")
        print(f"SKIP: Path already exist: {path}")
        return 0

