"""Script to install package from local build"""

#Imports
import os
import glob

#Finding build path based on build.py script location
file_path = os.path.dirname(__file__)
build_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

#Find build dir
build_dir = os.path.join(build_config_path, 'dist')
os.chdir(build_dir)

#Find wheels instalation file (getting only latest modified in catalogue)
file_name = glob.glob("*.whl")
file_name = sorted( file_name, key = os.path.getmtime)
file_path = os.path.join(build_dir, file_name[-1])

#Run build command
os.system("python3 -m pip install "+file_path)