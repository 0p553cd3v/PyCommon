#!/usr/bin/env python3

"""Script to run pylint linter"""

#Imports
import os
import yaml
import sys
from pylint.lint import Run

def main():

    #Print script start notification
    print('PyLint run started')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Read env.yaml to get project parameters
    with open(os.path.join('config', 'env.yml'), 'r') as file:
        ENV = yaml.safe_load(file) 

    #Define score value for a checker to accept code
    score = ENV['PYLINT_SCORE']

    pylint_args = ['./src', '--rcfile=tools/checkers/.pylintrc']

    #Run linter command
    pylint_results = Run(pylint_args, do_exit=False)
    if float(pylint_results.linter.stats.global_note) >= score:
        print("PyLint run finished - PASSED\n")
        return 0
    else:
        print("PyLint run finished - FAILED\n")
        return 1

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"PyLint run failed: {e}")
        sys.exit(1)