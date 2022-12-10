"""Script to run all tests"""

#Imports
import os

#Finding build path based on build.py script location
file_path = os.path.dirname(__file__)

#Changing directory to project config path
os.chdir(file_path)

#Run unit tests 
print('Unit tests - Test run')
os.system("python3 unit_tests/unit_tests_run.py")
#Run integration tests 
print('Integration tests - Test run')
os.system("python3 integration_tests/integration_tests_run.py")