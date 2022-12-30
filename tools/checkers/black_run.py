#!/usr/bin/env python3

"""Script to run black"""

#Imports
import os
import sys
import subprocess

def main():
    '''Main function to run script'''
    #Print script start notification
    print('Black run started')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Run black command

    subprocess.check_call(
        [
            "python3",
            "-m",
            "black",
            "--verbose",
            "./src",
        ]
    ) 

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Black run failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Black run failed: {e}")
        sys.exit(100)
    else:
        print('Black run finished - SUCCESS')   