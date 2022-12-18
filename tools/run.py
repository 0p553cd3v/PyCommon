#!/usr/bin/env python3

"""
Run all script (including code checkers, unit and integration tests, build and tests against package)
"""

#Imports
import os
import sys
import subprocess

#Define functions

def print_line_separator_with_title(title, separator, line_length):
    '''Function to print separation line with some title inside'''
    try:
        if len(separator) != 1:
            raise Exception("Separator length not equal to 1")
        if len(title) > line_length:
            raise Exception("Title length greater than line_length")
        #Initializing string of separators as a list
        separator_only_str=[]
        #Filling empty string with separators only
        for i in range(int(line_length) - len(title)):
            separator_only_str.append(separator)
        #Finding middle position of separator only string
        mid_pos = len(separator_only_str) // 2
        #Extending string as a list by title
        separation_line = separator_only_str[:mid_pos] + [title] + separator_only_str[mid_pos:]
        #Joining string as a list to create regular string
        separation_line = ''.join(separation_line)
        #print
        print(separation_line)
    except ValueError as e:
        print("Wrong function input value: " + str(e))
        sys.exit(1)
    except TypeError as e:
        print("Wrong function input type: " + str(e))
        sys.exit(1)
    except Exception as e:
        print("Exception: " + str(e))
        sys.exit(1)

#Main function def
def main():
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Set temporarily PYTHONPATH to src catalogue to fing source code of modules first
    os.environ["PYTHONPATH"] = os.path.join(project_config_path, "src")

    #Run black formater 
    print_line_separator_with_title(" Black formatter ","-",100)
    try:
        
        subprocess.check_call(
            [
                "tools/checkers/black_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        return e.returncode
    
    #Run vulture checker    
    print_line_separator_with_title(" Vulture dead code checker ","-",100)
    try:

        subprocess.check_call(
            [
                "tools/checkers/vulture_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        return e.returncode

    #Run lizard CCN analyzer 
    print_line_separator_with_title(" Lizard cyclomatic complexity analyzer ","-",100)
    try:
        
        subprocess.check_call(
            [
                "tools/checkers/lizard_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        return e.returncode

    #Run pylint checker
    print_line_separator_with_title(" PyLint linter checker ","-",100)
    try:
         
        subprocess.check_call(
            [
                "tools/checkers/pylint_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        return e.returncode

    #Run unit tests
    print_line_separator_with_title(" Unit tests ","-",100)
    try:
        subprocess.check_call(
            [
                "tests/unit_tests/unit_tests_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        return e.returncode

    #Run integration tests 
    print_line_separator_with_title(" Integration tests ","-",100)
    try:
        subprocess.check_call(
            [
                "tests/integration_tests/integration_tests_run.py",
            ]
        )
    except subprocess.CalledProcessError as e:
        print(f"Integration tests failed: {e.returncode}")
        return e.returncode

    #Run pyroma checker
    print_line_separator_with_title(" pyroma package config checker ","-",100)
    try:
         
        subprocess.check_call(
            [
                "tools/checkers/pyroma_run.py",
            ]
        ) 
    except subprocess.CalledProcessError as e:
        return e.returncode

    os.environ["PYTHONPATH"] = ""

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