#!/usr/bin/env python3

"""Script to run bandit"""

#Imports
import os
import sys
import yaml
import subprocess

def main():

    #Print script start notification
    print('Bandit run started')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Read env.yaml to get project parameters
    with open(os.path.join('config', 'env.yml'), 'r') as file:
        ENV = yaml.safe_load(file) 

    #Define lizard check parameters
    confidnece_lvl = ENV['BANDIT_CONFIDENCE_LVL']
    severity_lvl = ENV['BANDIT_SEVERITY_LVL']
    #Run black command

    subprocess.check_call(
        [
            "python3",
            "-m",
            "bandit",
            "-c",
            "pyproject.toml",
            str(confidnece_lvl),
            str(severity_lvl),
            "-r",
            "src",
        ]
    ) 
    
    print('Bandit run finished')

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Bandit run failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Bandit run failed: {e}")
        sys.exit(100)
    else:
        print('Bandit run finished - SUCCESS')  
    