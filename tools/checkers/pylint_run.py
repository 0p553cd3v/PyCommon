#!/usr/bin/env python3

"""Script to run unit tests only"""

#Imports
import os
from pylint.lint import Run

#Define score value for a checker to accept code
SCORE = 8.5

def main():
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    pylint_args = ['./src', '--rcfile=tools/checkers/.pylintrc']

    #Run linter command
    pylint_results = Run(pylint_args, do_exit=False)
    if float(pylint_results.linter.stats.global_note) >= SCORE:
        print("PASSED\n")
        return 0
    else:
        print("FAILED\n")
        return 1

if __name__ == "__main__":
    main()