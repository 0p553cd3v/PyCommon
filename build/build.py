#!/usr/bin/env python3

"""Script to build package."""

#Imports
import os
import sys
import subprocess

#Main function def
def main():
    """Run the script."""
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