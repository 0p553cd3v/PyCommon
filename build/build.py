#!/usr/bin/env python3

"""Script to build package"""

#Imports
import os
import sys
import subprocess
 
#Main function def
def main():
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    try:
        #    #Run test command
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
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e.returncode}")
    
#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e.returncode}")
        sys.exit(1)