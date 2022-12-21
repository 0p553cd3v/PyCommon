#!/usr/bin/env python3

"""Script to build package and run all tests against builded package"""

#Imports
import os
import sys
import subprocess

#Main function def
def main():
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    try:
        #Run test command
        print('Build - Build started')
        subprocess.check_call(
            [
                "build/build.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e.returncode}")

    try:
        #Run test command
        print('Tox - Installation and tests started')
        subprocess.check_call(
            [
                "tox",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        print(f"Instalation or tests failed failed: {e.returncode}")
    
#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e.returncode}")
        sys.exit(1)