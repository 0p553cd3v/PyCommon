#!/usr/bin/env python3

"""Script to run uniintegrationt tests only"""

#Imports
import os
import subprocess
import sys

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

    #Run test command
    m_run.run_subprocess_check_call("PyTest", "Integration tests",["pytest"], file_dir, repo_dir)  

#Main function call
if __name__ == "__main__":
    
    logger = m_log.get_logger()

    try:
        logger.info('PyTest run started - Integration tests')
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