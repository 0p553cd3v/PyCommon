#!/usr/bin/env python3

"""Script to setup the environment for package development."""

#Imports
import os
import sys
import subprocess

#Main function def
def main():
    """Run the script."""
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_run_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_run_path)

    #Run install command
    print('Development python packages installation started')
    subprocess.check_call(
        [
            #"sudo",
            "python3",
            "-m",
            "pip",
            "install",
            "-r",
            "./config/dev_requirements.txt"
        ]
    )
    print('Development python packages installation finished') 

    #Run install command
    print('Quality assurance packages installation started')
    subprocess.check_call(
        [
            #"sudo",
            "python3",
            "-m",
            "pip",
            "install",
            "-r",
            "./config/qa_requirements.txt"
        ]
    )
    print('Quality assurance packages installation finished') 

    #Run install command
    print('Python packages installation started')
    subprocess.check_call(
        [
            #"sudo",
            "python3",
            "-m",
            "pip",
            "install",
            "-r",
            "./config/requirements.txt"
        ]
    )
    print('Python packages installation finished') 

    #Import of common functions intentionally at this point as earlier dependencies can be missing
    sys.path.insert(1, './src')
    import yaml
    from py_common.sp_log import m_log
    from py_common.sp_env import m_conf
    from py_common.sp_file import m_file
    from py_common.sp_script import m_run

    logger = m_log.get_logger()
    cfg = m_conf.get_env_config_base()
    m_conf.generate_env_config_paths()

    #Read env.yaml to get project parameters
    with open(os.path.join('config', 'env.yml'), 'r') as file:
        ENV = yaml.safe_load(file)

    #Create pyenv python version file
    m_file.create_new_file(os.path.join('./.python-version'))

    #Read list of python interpreters 
    python_interpreters = list(ENV['PYTHON_INTERPRETERS'])

    m_run.run_subprocess_check_call("Install required pyenv versions", "pyenv install",["pyenv", "install", "-s"] + python_interpreters)

    #Add default system interpreter as a main one
    python_interpreters.insert(0,"system")

    #Write list of interpreters to python file
    m_file.write_content_to_empty_file(os.path.join('./.python-version'),python_interpreters)

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Environemnt setup failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Environemnt setup failed:  {e}")
        sys.exit(100)      
    else:
        print('Environemnt setup finished - SUCCESS')