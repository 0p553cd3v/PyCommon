#!/usr/bin/env python3

"""Script to run unit tests only"""

#Imports
import os
import subprocess
import sys
import yaml

from py_common.sp_script import m_run
from py_common.sp_log import m_log

#Main function def
def main():
    """Run the script."""

    #Finding build path based on build.py script location
    file_dir = os.path.dirname(__file__)
    repo_dir = os.path.abspath(os.path.join(file_dir, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(repo_dir)

    #Read env.yaml to get project parameters
    with open(os.path.join(repo_dir, 'config', 'env.yml'), 'r') as file:
        ENV = yaml.safe_load(file) 

    #Define score value for a checker to accept code
    cov_limit = ENV['UT_CODE_COVERAGE']

    #Run test command
    m_run.run_subprocess_check_call("PyTest", "Unit tests",["pytest", "--cov=py_common", "--cov-fail-under=" + str(cov_limit), "--cov-branch"], file_dir, repo_dir)    

#Main function call
if __name__ == "__main__":
    
    logger = m_log.get_logger()

    try:
        logger.info('PyTest run started - Unit tests')
        main()
    except subprocess.CalledProcessError as e:
        if e.returncode == 5:
            logger.info('PyTest run finished - No tests to run')
        else:
            logger.info(f"PyTest run failed: {e.returncode}")
            sys.exit(1)
    except Exception as e:
        logger.info(f"PyTest run failed: {e}")
        sys.exit(100)
    else:
        logger.info('PyTest run finished - SUCCESS')   

    
