#!/usr/bin/env python3

"""Script to setup the environemnt for package development"""

#Imports
import os
import os
import sys
import yaml
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
        print('Custom python packages installation started')
        subprocess.check_call(
            [
                "python3",
                "-m",
                "pip",
                "install",
                "-r",
                "./config/requirements.txt"
            ]
        ) 
    except subprocess.CalledProcessError as e:
        print(f"Custom python packages installation failed: {e.returncode}")
        raise subprocess.CalledProcessError from e
    
#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Environemnt setup failed: {e.returncode}")
        sys.exit(1)
    else:
        print('Environemnt setup finished - SUCCESS')