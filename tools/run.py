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
from py_common.base import prints

#Main function def
def main():
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Set temporarily PYTHONPATH to src catalogue to fing source code of modules first
    os.environ["PYTHONPATH"] = os.path.join(project_config_path, "src")

    #Run bandit security checker
    prints.print_line_separator_with_title(" Bandit security checker ","-",100)
    subprocess.check_call(
        [
                "tools/checkers/bandit_run.py",
        ]
    ) 

    #Run black formater 
    prints.print_line_separator_with_title(" Black formatter ","-",100)
    subprocess.check_call(
        [
            "tools/checkers/black_run.py",
        ]
    ) 
    
    #Run vulture checker    
    prints.print_line_separator_with_title(" Vulture dead code checker ","-",100)
    subprocess.check_call(
        [
            "tools/checkers/vulture_run.py",
        ]
    ) 

    #Run lizard CCN analyzer 
    prints.print_line_separator_with_title(" Lizard cyclomatic complexity analyzer ","-",100)
    subprocess.check_call(
        [
            "tools/checkers/lizard_run.py",
        ]
    ) 

    #Run pylint checker
    prints.print_line_separator_with_title(" PyLint linter checker ","-",100)
    subprocess.check_call(
        [
            "tools/checkers/pylint_run.py",
        ]
    ) 

    #Run unit tests
    prints.print_line_separator_with_title(" Unit tests ","-",100)
    subprocess.check_call(
        [
            "tests/unit_tests/unit_tests_run.py",
        ]
    ) 

    #Run integration tests 
    prints.print_line_separator_with_title(" Integration tests ","-",100)
    subprocess.check_call(
        [
            "tests/integration_tests/integration_tests_run.py",
        ]
    )
    
    #Run docstr coverage checker
    prints.print_line_separator_with_title(" docstr coverage checker ","-",100)
    subprocess.check_call(
        [
            "tools/checkers/docstrcov_run.py",
        ]
    ) 

    #Run pyroma checker
    prints.print_line_separator_with_title(" pyroma package config checker ","-",100)
    subprocess.check_call(
        [
            "tools/checkers/pyroma_run.py",
        ]
    ) 

    os.environ["PYTHONPATH"] = ""

    #Run Build and test script
    prints.print_line_separator_with_title(" Build and test package ","-",100)
    subprocess.check_call(
        [
            "tools/build_and_test.py",
        ]
    )

    #Run dccoumentation builder script
    prints.print_line_separator_with_title(" Generate documentation ","-",100)
    subprocess.check_call(
        [
            "docs/gen_doc.py",
        ]
    )

    #Run cleaunup script
    prints.print_line_separator_with_title(" Cleanup artifacts ","-",100)
    subprocess.check_call(
        [
            "tools/cleanup.py",
        ]
    )

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Run script failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Run script failed:  {e}")
        sys.exit(100)
    else:
        print('Run script finished - SUCCESS')