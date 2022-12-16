#!/usr/bin/env python3

"""Script to run unit tests only"""

#Imports
import os
import subprocess
import sys

#Main function def
def main():
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)

    #Changing directory to project config path
    os.chdir(file_path)

    try:
        #    #Run test command
        print('Unit tests - Test run')
        subprocess.check_call(
            [
                "pytest",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        print(f"Pytest failed: {e.returncode}")
    
#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e.returncode}")
        sys.exit(1)
