#!/usr/bin/env python3

"""Script to build package"""

#Imports
import os
import sys
import subprocess

#Adding path to sys to use local function defined in src folder
sys.path.append("src")
from py_common.file import dir


#Main function def
def main():
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Run build command
    print('Build - Build run')
    subprocess.check_call(
        [
            "python3",
            "-m",
            "build",
            "--sdist",
            "--wheel",
            "--outdir",
            "dist/",
        ]
    ) 
    #Run cleanup commands
    print('Build - Cleanup run')
    dir.clean_up_folder_starting_with("build","lib")
    dir.clean_up_folder_starting_with("build","bdist")

    
#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Build failed:  {e}")
        sys.exit(100)  
    else:
        print('Build finished - SUCCESS')    