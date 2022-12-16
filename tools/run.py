#!/usr/bin/env python3

"""
Run all script (including code checkers, unit and integration tests, build and tests against package)
"""

#Imports
import os
import sys
import subprocess

#Main function def
def main():
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Set temporarily PYTHONPATH to src catalogue to fing source code of modules first
    os.environ["PYTHONPATH"] = os.path.join(project_config_path, "src")

    try:
        #Run pylint checker 
        print('PyLint - Checker run')
        subprocess.check_call(
            [
                "tools/checkers/pylint_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        print(f"PyLint failed: {e.returncode}")
    
    try:
        #Run unit tests
        print('Unit tests - Test run')
        subprocess.check_call(
            [
                "tests/unit_tests/unit_tests_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        print(f"Unit tests failed: {e.returncode}")

    try:
        #Run integration tests 
        print('Integration tests - Test run')
        subprocess.check_call(
            [
                "tests/integration_tests/integration_tests_run.py",
            ]
        )
    except subprocess.CalledProcessError as e:
        print(f"Integration tests failed: {e.returncode}")

    os.environ["PYTHONPATH"] = ""

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e.returncode}")
        sys.exit(1)
