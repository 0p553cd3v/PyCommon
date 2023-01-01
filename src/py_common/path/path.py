"""Path module."""

# Imports
import os

# Functions
def parent_path(path):
    """Function to return parent directory from given directory or path."""
    return os.path.abspath(os.path.join(path, os.pardir))
