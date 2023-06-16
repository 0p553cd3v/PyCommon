import os
import pytest
import filecmp
from py_common.sp_script import m_run 

def test_run_subprocess_check_call(capsys,create_test_project_env):
    '''Main path test on running command'''
    #Finding build path based on build.py script location
    test_repo_dir = create_test_project_env[1]
    os.chdir(test_repo_dir)

    test_dir = os.path.join(test_repo_dir, "test_path")
    os.mkdir(test_dir)
    os.chdir(test_repo_dir)
    result = m_run.run_subprocess_check_call("Touch", "Create file", ["touch", "test_file.txt"], test_dir, test_repo_dir)
    #Assert commandHandler
    out, err = capsys.readouterr()
    assert out.strip() == "----------------------------------------Touch - Create file-----------------------------------------"
    assert os.path.exists(os.path.join(test_dir,"test_file.txt"))
    assert result == 0

def test_run_subprocess_check_call_when_exceptions(create_test_project_env,capsys):
    '''Alternative path test on running command with exception'''
    test_repo_dir = create_test_project_env[1]
    os.chdir(test_repo_dir)

    test_dir = os.path.join(test_repo_dir, os.path.pardir)
    os.chdir(test_repo_dir)
    with pytest.raises(SystemExit) as exc_info:
        result = m_run.run_subprocess_check_call("Touch", "Create file", ["touch", "-broken", "test_file.txt"], test_dir, test_repo_dir)
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 1
    assert not os.path.exists(os.path.join(test_dir,"test_file.txt"))

def test_run_subprocess_check_call_when_dirs_null(create_test_project_env,capsys):
    '''Main path test on running command'''
    #Finding build path based on build.py script location
    test_repo_dir = create_test_project_env[1]
    os.chdir(test_repo_dir)

    result = m_run.run_subprocess_check_call("Touch", "Create file", ["touch", "test_file.txt"])
    #Assert commandHandler
    out, err = capsys.readouterr()
    assert out.strip() == "----------------------------------------Touch - Create file-----------------------------------------"
    assert os.path.exists(os.path.join(test_repo_dir,"test_file.txt"))
    assert result == 0

def test_run_subprocess_check_call_when_one_pipe(capsys,create_test_project_env):
    '''Alternative path test on running command with one pipe'''
    #Finding build path based on build.py script location
    test_repo_dir = create_test_project_env[1]
    os.chdir(test_repo_dir)
    test_dir = os.path.join(test_repo_dir, "test_path")
    os.mkdir(test_dir)
    os.chdir(test_dir)
    file_content = [
        "1st line",
    ]
    with open('test_file.txt', 'w') as fp:
        fp.write('\n'.join(str(item) for item in file_content))
    os.chdir(test_repo_dir)
    result = m_run.run_subprocess_check_call("Read", "Read file", ["cat", "test_file.txt" ,"|", "grep", "-q", "1st line"], test_dir, test_repo_dir)
    #Assert commandHandler
    out, err = capsys.readouterr()
    assert out.strip() == "------------------------------------------Read - Read file------------------------------------------"
    assert result == 0

def test_run_subprocess_check_call_when_two_pipes(capsys,create_test_project_env):
    '''Alternative path test on running command with two pipes'''
    #Finding build path based on build.py script location
    test_repo_dir = create_test_project_env[1]
    os.chdir(test_repo_dir)
    test_dir = os.path.join(test_repo_dir, "test_path")
    os.mkdir(test_dir)
    os.chdir(test_dir)
    file_content = [
        "1st line",
        "2nd line",
        "3rd line",
        "4th end",
    ]
    with open('test_file.txt', 'w') as fp:
        fp.write('\n'.join(str(item) for item in file_content))
    os.chdir(test_repo_dir)
    result = m_run.run_subprocess_check_call("Read", "Read file", ["cat", "test_file.txt" ,"|", "grep", "end", "|", "grep", "-q", "4th end"], test_dir, test_repo_dir)
    #Assert commandHandler
    out, err = capsys.readouterr()
    assert out.strip() == "------------------------------------------Read - Read file------------------------------------------"
    assert result == 0