#!/usr/bin/env python3

"""Run all script (including code checkers, unit and integration tests, build and tests against package and generate documentation)."""

#Imports
import os
import sys
import yaml
import subprocess

#Define functions

#Adding path to sys to use local function defined in src folder
sys.path.append("src")
from py_common.sp_log import m_log
from py_common.sp_script import m_run
from py_common.sp_env import m_conf

#Main function def
def main():
    """Run the script."""
    file_dir = os.path.dirname(__file__)
    repo_dir = os.path.abspath(os.path.join(file_dir, os.pardir))

    #Changing directory to project config path
    os.chdir(repo_dir)

    #Setup logger instance
    logger = m_log.get_logger()

    #Set temporarily PYTHONPATH to src catalogue to fing source code of modules first
    os.environ["PYTHONPATH"] = os.path.join(repo_dir, "src")

    #Read env.yaml to get project parameters
    with open(os.path.join('config', 'env.yml'), 'r') as file:
        ENV = yaml.safe_load(file) 

    #Run bandit security checker
    confidnece_lvl = ENV['BANDIT_CONFIDENCE_LVL']
    severity_lvl = ENV['BANDIT_SEVERITY_LVL']
    m_run.run_subprocess_check_call("Bandit", "Security checker",["python3", "-m", "bandit", "-c", "pyproject.toml", str(confidnece_lvl), str(severity_lvl), "-r", "src"])

    #Run black formater 
    m_run.run_subprocess_check_call("Black", "Formatter",["python3", "-m", "black", "--verbose", "./src"])
    
    #Run vulture checker
    m_run.run_subprocess_check_call("Vuluture", "Dead code checker",["python3", "-m", "vulture"])    

    #Run lizard CCN analyzer 
    ccn_limit = ENV['LIZARD_CCN']
    length_limit = ENV['LIZARD_LENGTH']
    param_limit = ENV['LIZARD_PAR_COUNT']
    nloc_limit = ENV['LIZARD_NLOC']
    m_run.run_subprocess_check_call("Lizard", "CCN analyzer",["lizard", "src/", "-V", "-Tcyclomatic_complexity=" + str(ccn_limit), "-Tlength=" + str(length_limit), "-Tparameter_count=" + str(param_limit), "-Tnloc=" + str(nloc_limit)])  

    #Run pylint checker
    m_run.run_subprocess_check_call("PyLint", "Linter",["pylint", "--rcfile=./pyproject.toml", "./src",])

    #Run unit tests
    subprocess.check_call("tests/unit_tests/unit_tests_run.py") 

    #Run integration tests 
    subprocess.check_call("tests/integration_tests/integration_tests_run.py")
     
    #Run docstr coverage checker
    docstrcov_min_score = ENV['DOCSTRING_COVERAGE']
    m_run.run_subprocess_check_call("dockstrcov", "Documentation coverage checker",["docstr-coverage", "./src", "./tools", "./build/build.py", "--fail-under=" + str(docstrcov_min_score), "-i", "-P", "-m"])

    #Run pydocstyle checker
    m_run.run_subprocess_check_call("pydocstyle", "Documentation style checker",["pydocstyle", "./src", "./tools", "./build/build.py", "./docs/gen_doc.py"])

    #Run pyroma checker
    pyroma_min_score = ENV['PYROMA_MIN']
    m_run.run_subprocess_check_call("pyroma", "Config checker",["python3", "-m", "pyroma", ".", "--min", str(pyroma_min_score)])

    os.environ["PYTHONPATH"] = ""

    #Run Build and test script
    subprocess.check_call("tools/build_and_test.py", env=os.environ)

    #Run dccoumentation builder script
    subprocess.check_call("docs/gen_doc.py")

    #Run cleaunup script
    subprocess.check_call("tools/cleanup.py")

#Main function call
if __name__ == "__main__":
    
    logger = m_log.get_logger()
    cfg = m_conf.get_env_conf_all()

    try:
        logger.info('Run script started')
        main()
    except subprocess.CalledProcessError as e:
        logger.error(f"Run script failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Run script failed:  {e}")
        sys.exit(100)
    else:
        logger.info('Run script finished - SUCCESS')