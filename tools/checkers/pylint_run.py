#!/usr/bin/env python3

"""Script to run unit tests only"""

#Imports
import os
import yaml
from pylint.lint import Run

#Read env.yaml to get project parameters
with open(os.path.join(os.path.dirname(__file__), os.pardir,'config', 'env.yml'), 'r') as file:
    ENV = yaml.safe_load(file) 

#Define score value for a checker to accept code
score = ENV['PYLINT_SCORE']

def main():
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    pylint_args = ['./src', '--rcfile=tools/checkers/.pylintrc']

    #Run linter command
    pylint_results = Run(pylint_args, do_exit=False)
    if float(pylint_results.linter.stats.global_note) >= score:
        print("PASSED\n")
        return 0
    else:
        print("FAILED\n")
        return 1

if __name__ == "__main__":
    main()