#!/usr/bin/env python3

"""Script to run unit tests only"""

#Imports
import os
import subprocess
import sys

#Main function def
def main():
    
    #Print script start notification
    print('PyTest run started - Unit tests')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)

    #Changing directory to project config path
    os.chdir(file_path)

    #Run test command

    subprocess.check_call(
        [
            "pytest",
        ]
    ) 
    print('PyTest run finished - Unit tests')

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        if e.returncode == 5:
            print('PyTest run finished - No tests to run')
        else:
            print(f"PyTest run failed: {e.returncode}")
            sys.exit(1)
    except Exception as e:
        print(f"PyTest run failed: {e}")
        sys.exit(1)

    
