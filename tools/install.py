#!/usr/bin/env python3
 
"""Script to install package from local build."""

#Imports
import os
import glob
import sys
import subprocess

#Adding path to sys to use local function defined in src folder
sys.path.append("src")
from py_common.log import log

#Main function def
def main():
    """Run the script."""
    #Finding build path based on install.py script location
    file_path = os.path.dirname(__file__)
    build_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Find build dir
    build_dir = os.path.join(build_config_path, 'dist')
    os.chdir(build_dir)


    #Find wheels instalation file (getting only latest modified in catalogue)
    file_name = glob.glob("*.whl")
    file_name = sorted( file_name, key = os.path.getmtime)
    file_path = os.path.join(build_dir, file_name[-1])

    #Run installation command
    print('Local installation - Installation started')
    subprocess.check_call(
        [
            "python3",
            "-m",
            "pip",
            "install",
            file_path,
        ]
    ) 

#Main function call
if __name__ == "__main__":
    
    logger = log.get_logger()

    try:
        logger.info('Installation started')
        main()
    except subprocess.CalledProcessError as e:
        logger.exception(f"Installation failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Installation failed:  {e}")
        sys.exit(100)    
    else:
        logger.info('Installation finished - SUCCESS')