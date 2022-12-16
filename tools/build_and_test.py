#!/usr/bin/env python3

"""Script to run all tests"""

#Imports
import os

#Finding build path based on build.py script location
file_path = os.path.dirname(__file__)
project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

#Changing directory to project config path
os.chdir(project_config_path)

#Prepare new build
os.system("python3 build/build.py")

#Run build 
os.system("tox")
