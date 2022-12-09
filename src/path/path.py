import os

def parent_path(path):
    return os.path.abspath(os.path.join(path, os.pardir))