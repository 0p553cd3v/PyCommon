import os
import subprocess
import pytest
from py_common.file import dir 

def test_create_dir_when_dir_exist(tmp_path, capsys):
    '''Simple test to assert if custom create dir function is not generating directories if they exist and do not fail if exist'''
    d = tmp_path / "existing_dir"
    d.mkdir()
    dir.create_dir(d)
    out, err = capsys.readouterr()
    assert out.strip() == "SKIP: Path already exist: " + str(d)
    assert err == ''

def test_create_dir_when_dir_not_exist(tmp_path, capsys):
    '''Simple test to assert if custom create dir function is generating directories if they do not exist and do not fail if exist'''
    d = tmp_path / "new_dir"
    assert not os.path.exists(d)
    dir.create_dir(d)
    out, err = capsys.readouterr()
    assert out.strip() == "SUCCESS: Directory " + str(d) + " succesfully created"
    assert err == ''
    assert os.path.exists(d)

def test_create_dir_when_user_has_no_edit_permission(tmp_path, capsys):
    '''Simple test to assert if custom create dir function is failing if direcotry do not exist but no permission to make it'''
    p = tmp_path / "parent_dir"
    p.mkdir()
    assert os.path.exists(p)
    subprocess.run(
        [
            "chmod",
            "244",
            str(os.path.abspath(p)),
        ]
    ) 
    d = p / "new_dir"
    assert not os.path.exists(d)
    dir.create_dir(d)
    out, err = capsys.readouterr()
    assert out.strip() == "Permission denied during directory creation: " + str(d) 
    subprocess.run(
        [
            "chmod",
            "777",
            str(os.path.abspath(p)),
        ]
    ) 
