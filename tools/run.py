#!/usr/bin/env python3

"""
Run all script (including code checkers, unit and integration tests, build and tests against package)
"""

#Imports
import os
import sys
import subprocess

#Define functions

#Adding path to sys to use local function defined in src folder
sys.path.append("src")
from py_common.base import print

#Main function def
def main():
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Set temporarily PYTHONPATH to src catalogue to fing source code of modules first
    os.environ["PYTHONPATH"] = os.path.join(project_config_path, "src")

    #Run bandit security checker
    print.print_line_separator_with_title(" Bandit security checker ","-",100)
    try:
         
        subprocess.check_call(
            [
                "tools/checkers/bandit_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError from e

    #Run black formater 
    print.print_line_separator_with_title(" Black formatter ","-",100)
    try:
        
        subprocess.check_call(
            [
                "tools/checkers/black_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError from e
    
    #Run vulture checker    
    print.print_line_separator_with_title(" Vulture dead code checker ","-",100)
    try:

        subprocess.check_call(
            [
                "tools/checkers/vulture_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError from e

    #Run lizard CCN analyzer 
    print.print_line_separator_with_title(" Lizard cyclomatic complexity analyzer ","-",100)
    try:
        
        subprocess.check_call(
            [
                "tools/checkers/lizard_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError from e

    #Run pylint checker
    print.print_line_separator_with_title(" PyLint linter checker ","-",100)
    try:
         
        subprocess.check_call(
            [
                "tools/checkers/pylint_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError from e

    #Run unit tests
    print.print_line_separator_with_title(" Unit tests ","-",100)
    try:
        subprocess.check_call(
            [
                "tests/unit_tests/unit_tests_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError from e

    #Run integration tests 
    print.print_line_separator_with_title(" Integration tests ","-",100)
    try:
        subprocess.check_call(
            [
                "tests/integration_tests/integration_tests_run.py",
            ]
        )
    except subprocess.CalledProcessError as e:
        print(f"Integration tests failed: {e.returncode}")
        raise subprocess.CalledProcessError from e
    
    #Run docstr coverage checker
    print.print_line_separator_with_title("docstr coverage checker ","-",100)
    try:
         
        subprocess.check_call(
            [
                "tools/checkers/docstrcov_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError from e

    #Run pyroma checker
    print.print_line_separator_with_title("pyroma package config checker ","-",100)
    try:
         
        subprocess.check_call(
            [
                "tools/checkers/pyroma_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError from e

    os.environ["PYTHONPATH"] = ""

    #Run Build and test script
    print.print_line_separator_with_title("Build and test package ","-",100)
    try:
         
        subprocess.check_call(
            [
                "tools/build_and_test.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        raise subprocess.CalledProcessError from e

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Run script failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Run script failed:  {e}")
        sys.exit(1)
    else:
        print('Run script finished - SUCCESS')