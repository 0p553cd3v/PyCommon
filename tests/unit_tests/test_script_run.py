import os
import pytest
import subprocess
from pathlib import Path
from py_common.sp_script import m_run 

def test_run_subprocess_check_call(tmp_path,capsys):
    '''Main path test on running command'''
    text_to_print = "Text"
    #Finding build path based on build.py script location
    file_dir = os.path.dirname(__file__)
    repo_dir = os.path.abspath(os.path.join(file_dir, os.pardir,os.pardir))

    d = os.path.join(tmp_path, "test_path")
    os.mkdir(d)
    os.chdir(tmp_path)
    result = m_run.run_subprocess_check_call("Touch", "Create file", ["touch", "test_file.txt"], d, repo_dir)
    #Assert commandHandler
    out, err = capsys.readouterr()
    assert os.getcwd() == d
    assert out.strip() == "----------------------------------------Touch - Create file-----------------------------------------"
    assert result == 0
    assert os.path.exists(os.path.join(d,"test_file.txt"))

def test_run_subprocess_check_call_when_exceptions(tmp_path,capsys):
    '''Alternative path test on running command with exception'''
    text_to_print = "Text"
    #Finding build path based on build.py script location
    file_dir = os.path.dirname(__file__)
    repo_dir = os.path.abspath(os.path.join(file_dir, os.pardir,os.pardir))

    d = tmp_path
    with pytest.raises(SystemExit) as exc_info:
        result = m_run.run_subprocess_check_call("Touch", "Create file", ["touch", "-broken", "test_file.txt"], d, repo_dir)
    assert exc_info.type == SystemExit
    assert Path(os.getcwd()) == d
    assert exc_info.value.code == 1
    assert not os.path.exists(os.path.join(d,"test_file.txt"))

def test_run_subprocess_check_call_when_dirs_null(tmp_path,capsys):
    '''Alternative path test on running command when dirs not specified and run not from repo'''
    text_to_print = "Text"
    #Finding build path based on build.py script location
    file_dir = os.path.dirname(__file__)
    repo_dir = os.path.abspath(os.path.join(file_dir, os.pardir,os.pardir))
    
    d = os.path.join(tmp_path, "test_path")
    os.mkdir(d)
    os.chdir(d)

    with pytest.raises(FileNotFoundError) as exc_info:
        result = m_run.run_subprocess_check_call("Touch", "Create file", ["touch", "-broken", "test_file.txt"])
    assert exc_info.type == FileNotFoundError
    #Assert commandHandler
    assert os.getcwd() == d

def test_run_subprocess_check_call_when_run_dir_null_and_repo_dir_spec(tmp_path,capsys):
    '''Alternative path test on running command when dirs not specified and run not from repo'''
    text_to_print = "Text"
    #Finding build path based on build.py script location
    file_dir = os.path.dirname(__file__)
    repo_dir = os.path.abspath(os.path.join(file_dir, os.pardir,os.pardir))
    
    d = os.path.join(tmp_path, "test_path")
    os.mkdir(d)
    os.chdir(d)

    result = m_run.run_subprocess_check_call("Touch", "Create file", ["touch", "test_file.txt"], "", repo_dir)
    #Assert commandHandler
    assert os.getcwd() == d
    out, err = capsys.readouterr()
    assert out.strip() == "----------------------------------------Touch - Create file-----------------------------------------"
    assert result == 0
    assert os.path.exists(os.path.join(d,"test_file.txt"))


