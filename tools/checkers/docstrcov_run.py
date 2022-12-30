#!/usr/bin/env python3

"""Script to run docstring coveradge"""

#Imports
import os
import sys
import yaml
import subprocess

def main():
    '''Main function to run script'''
    #Print script start notification
    print('Docstring coverage run started')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Read env.yaml to get project parameters
    with open(os.path.join('config', 'env.yml'), 'r') as file:
        ENV = yaml.safe_load(file) 

    #Define score value for a checker to accept code
    min_score = ENV['DOCSTRING_COVERAGE']

    #Run Docstring coverage command

    subprocess.check_call(
        [
            "docstr-coverage",
            "./src",
            "./tools",
            "./build/build.py",
            "--fail-under=" + str(min_score),
            "-i", #ignore __init__ files
            "-P", #skip private functions
            "-m", #ignore magic files exceppt __init__
        ]
    ) 

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Docstring coverage run failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Docstring coverage run failed: {e}")
        sys.exit(100)
    else:
        print('Docstring coverage run finished - SUCCESS')   