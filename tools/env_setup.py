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

    #Run test command
    print('Custom python packages installation started')
    subprocess.check_call(
        [
            "sudo",
            "python3",
            "-m",
            "pip",
            "install",
            "-r",
            "./config/requirements.txt"
        ]
    )
    print('Custom python packages installation finished') 
    
#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Environemnt setup failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Environemnt setup failed:  {e}")
        sys.exit(100)      
    else:
        print('Environemnt setup finished - SUCCESS')