#!/usr/bin/env python3

"""Script to build package and run all tests against builded package."""

#Imports
import os
import sys
import subprocess
import yaml
import shutil
import time

#Adding path to sys to use local function defined in src folder
sys.path.append("src")
from py_common.sp_script import m_run
from py_common.sp_log import m_log
from py_common.sp_file import m_file

#Main function def
def main():
    """Run the script."""
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Read env.yaml to get project parameters
    with open(os.path.join('config', 'env.yml'), 'r') as file:
        ENV = yaml.safe_load(file)

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Run run build command
    subprocess.check_call("build/build.py") 

    #Create pyenv python version file
    m_file.create_new_file(os.path.join('./.python-version'))

    #Read list of python interpreters 
    python_interpreters = ENV['PYTHON_INTERPRETERS']

    #Write list of interpreters to python file
    m_file.write_content_to_empty_file(os.path.join('./.python-version'),python_interpreters)

    #Run tox command
    #m_run.run_subprocess_check_call("Install tox for pyenv - if used", "tox installer",["python3", "-m", "pip", "install", "tox<4", "tox-pyenv", "py"])

    #Run tox command
    m_run.run_subprocess_check_call("Tox", "venv checker",["python3", "-m", "tox"])

    #Remove pyenv python version file
    os.remove(os.path.join('./.python-version'))

    #Remove tox env
    shutil.rmtree(os.path.join('./.tox/'))       
    
#Main function call
if __name__ == "__main__":
    
    logger = m_log.get_logger()
    
    try:
        logger.info('Build and test started')
        main()
    except subprocess.CalledProcessError as e:
        logger.exception(f"Build and test failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Build and test failed:  {e}")
        sys.exit(100)  
    else:
        logger.info('Build and test finished - SUCCESS')
    