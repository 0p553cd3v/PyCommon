#!/usr/bin/env python3

"""Script to build package and run all tests against builded package"""

#Imports
import os
import sys
import subprocess

#Main function def
def main():
    ''''Main function to run script'''
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Run run build command
    print('Build - Build started')
    subprocess.check_call(
        [
            "build/build.py",
        ]
    ) 

    #Run tox command
    print('Tox - Installation and tests started')
    subprocess.check_call(
        [
            "tox",
        ]
    ) 
    
#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Build and test failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Build and test failed:  {e}")
        sys.exit(100)  
    else:
        print('Build and test finished - SUCCESS')
    