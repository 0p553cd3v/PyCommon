#!/usr/bin/env python3

"""Script to run pylint linter"""

#Imports
import os
import yaml
import sys
import subprocess
from pylint.lint import Run

def main():

    #Print script start notification
    print('PyLint run started')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Run pylint command

    subprocess.check_call(
        [
            "pylint",
            "--rcfile=./pyproject.toml",
            "./src",
        ]
    ) 

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"PyLint run failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"PyLint run failed: {e}")
        sys.exit(100)
    else:
        print('PyLint run finished - SUCCESS')