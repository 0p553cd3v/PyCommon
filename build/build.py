"""Script to build package"""

#Imports
import os

#Finding build path based on build.py script location
file_path = os.path.dirname(__file__)
build_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

#Changing directory to build config path
os.chdir(build_config_path)

#Run build command
os.system("python3 -m build")
 
