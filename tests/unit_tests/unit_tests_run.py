"""Script to run unit tests only"""

#Imports
import os

#Finding build path based on build.py script location
file_path = os.path.dirname(__file__)
project_config_path = os.path.abspath(os.path.join(file_path, os.pardir, os.pardir))

#Changing directory to project config path
os.chdir(project_config_path)

#Run test command
os.system("python3 -m pytest -m unit")