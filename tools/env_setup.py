#!/usr/bin/env python3

"""Script to setup the environment for package development."""

#Imports
import os
import sys
import subprocess

#Main function def
def main():
    """Run the script."""
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_run_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_run_path)

    #Run install command
    print('Custom python packages installation started')
    subprocess.check_call(
        [
            #"sudo",
            "python3",
            "-m",
            "pip",
            "install",
            "-r",
            "./config/requirements.txt"
        ]
    )
    print('Custom python packages installation finished') 

    #Import of common functions intentionally at this point as earlier dependencies can be missing
    sys.path.insert(1, './src')
    from py_common.path import path
    from py_common.file import dir
    from py_common.log import log

    logger = log.get_logger()
    
    
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