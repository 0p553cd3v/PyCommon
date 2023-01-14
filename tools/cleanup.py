#!/usr/bin/env python3

"""Script to cleanup run artifacts from repository."""

#Imports
import os
import sys
import subprocess

#Adding path to sys to use local function defined in src folder
sys.path.append("src")
from py_common.sp_file import m_dir
from py_common.sp_log import m_log

#Main function def
def main():
    """Run the script."""
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Run build command
    print('Cleanup run')

    #Run cleanup commands
    print('Cleanup - Build artifacts')
    m_dir.clean_up_folder_starting_with("build","lib")
    m_dir.clean_up_folder_starting_with("build","bdist")

    
#Main function call
if __name__ == "__main__":
    
    logger = m_log.get_logger()
    
    try:
        logger.info('Cleanup started')
        main()
    except subprocess.CalledProcessError as e:
        logger.exception(f"Cleanup failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Cleanup failed:  {e}")
        sys.exit(100)  
    else:
        logger.info('Cleanup finished - SUCCESS')    