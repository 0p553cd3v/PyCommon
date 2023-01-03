#!/usr/bin/env python3

"""Script to run unit tests only"""

#Imports
import os
import subprocess
import sys
import yaml

#Main function def
def main():
    """Run the script."""
    #Print script start notification
    print('PyTest run started - Unit tests')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(file_path)

    #Read env.yaml to get project parameters
    with open(os.path.join(project_config_path, 'config', 'env.yml'), 'r') as file:
        ENV = yaml.safe_load(file) 

    #Define score value for a checker to accept code
    cov_limit = ENV['UT_CODE_COVERAGE']

    #Run test command

    subprocess.check_call(
        [
            "pytest",
            "--cov=py_common",
            "--cov-fail-under=" + str(cov_limit),
            "--cov-branch",
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
        sys.exit(100)
    else:
        print('PyTest run finished - SUCCESS')   

    
