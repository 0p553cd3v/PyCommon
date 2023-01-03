#!/usr/bin/env python3

"""Script to run pyroma checker for dead code."""

#Imports
import os
import sys
import yaml
import subprocess

def main():
    """Run the script."""
    #Print script start notification
    print('pyroma run started')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Read env.yaml to get project parameters
    with open(os.path.join('config', 'env.yml'), 'r') as file:
        ENV = yaml.safe_load(file) 

    #Define score value for a checker to accept code
    min_score = ENV['PYROMA_MIN']

    #Run pyroma command

    subprocess.check_call(
        [
            "python3",
            "-m",
            "pyroma",
            ".",
            "--min",
            str(min_score),
        ]
    ) 

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"pyroma run failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"pyroma run failed: {e}")
        sys.exit(100)
    else:
        print('pyroma run finished - SUCCESS')
        