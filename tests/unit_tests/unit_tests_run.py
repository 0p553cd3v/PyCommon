"""Script to run unit tests only"""

#Imports
import os

#Finding build path based on build.py script location
file_path = os.path.dirname(__file__)

#Changing directory to project config path
os.chdir(file_path)

#Run test command
os.system("pytest")
