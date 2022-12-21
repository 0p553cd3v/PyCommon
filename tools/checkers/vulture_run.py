#!/usr/bin/env python3

"""Script to run vulture checker for dead code"""

#Imports
import os
import sys
import subprocess

def main():

    #Print script start notification
    print('Vulture run started')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Run vulture command

    subprocess.check_call(
        [
            "python3",
            "-m",
            "vulture",
        ]
    ) 
    
    print('Vulture run finished')

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Vulture run failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Vulture run failed: {e}")
        sys.exit(1)