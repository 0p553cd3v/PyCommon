#!/usr/bin/env python3

"""Script to run lizard CCN analyzer"""

#Imports
import os
import subprocess
import sys
import yaml

#Main function def
def main():
    
    #Print script start notification
    print('Lizard run started')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Read env.yaml to get project parameters
    with open(os.path.join('config', 'env.yml'), 'r') as file:
        ENV = yaml.safe_load(file) 

    #Define lizard check parameters
    ccn_limit = ENV['LIZARD_CCN']
    length_limit = ENV['LIZARD_LENGTH']
    param_limit = ENV['LIZARD_PAR_COUNT']
    nloc_limit = ENV['LIZARD_NLOC']

    #Run test command

    subprocess.check_call(
        [
            "lizard",
            "src/",
            "-V",
            "-Tcyclomatic_complexity=" + str(ccn_limit),
            "-Tlength=" + str(length_limit),
            "-Tparameter_count=" + str(param_limit),
            "-Tnloc=" + str(nloc_limit),  
        ]
    )

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Lizard run failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Lizard run failed: {e}")
        sys.exit(1)
    else:
        print('Lizard run finished - SUCCESS')      

    
