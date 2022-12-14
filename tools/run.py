import os

file_path = os.path.dirname(__file__)
project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

#Changing directory to project config path
os.chdir(project_config_path)

#Set temporarily PYTHONPATH to src catalogue to fing source code of modules first
os.environ["PYTHONPATH"] = os.path.join(project_config_path, "src")

#Run unit tests 
print('Unit tests - Test run')
os.system("python3 tests/unit_tests/unit_tests_run.py")

#Run integration tests 
print('Integration tests - Test run')
os.system("python3 tests/integration_tests/integration_tests_run.py")

os.environ["PYTHONPATH"] = ""