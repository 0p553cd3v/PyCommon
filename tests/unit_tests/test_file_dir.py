import os
import subprocess
import pytest
from py_common.file import dir 

def test_create_dir_when_dir_exist(tmp_path, capsys):
    '''Simple test to assert if custom create dir function is not generating directories if they exist and do not fail if exist'''
    d = tmp_path / "existing_dir"
    d.mkdir()
    result = dir.create_dir_if_not_exist(d)
    out, err = capsys.readouterr()
    assert result == True
    assert out.strip() == "SKIP: Path already exist: " + str(d)
    assert err == ''

def test_create_dir_when_dir_not_exist(tmp_path, capsys):
    '''Simple test to assert if custom create dir function is generating directories if they do not exist and do not fail if exist'''
    d = tmp_path / "new_dir"
    assert not os.path.exists(d)
    result = dir.create_dir_if_not_exist(d)
    out, err = capsys.readouterr()
    assert result == True
    assert out.strip() == "SUCCESS: Directory " + str(d) + " succesfully created"
    assert err == ''
    assert os.path.exists(d)

def test_create_dir_when_user_has_no_edit_permission(tmp_path):
    '''Simple test to assert if custom create dir function is failing if direcotry do not exist but no permission to make it'''
    p = tmp_path / "parent_dir"
    p.mkdir()
    assert os.path.exists(p)
    subprocess.run(
        [
            "chmod",
            "-w",
            str(p),
        ]
    ) 
    d = p / "new_dir"
    assert not os.path.exists(d)
    with pytest.raises(PermissionError) as exc_info:
        dir.create_dir_if_not_exist(d)
    assert exc_info.type == PermissionError
    subprocess.run(
        [
            "chmod",
            "+w",
            str(p),
        ]
    ) 

def test_clean_up_folder_starting_with(tmp_path, capsys):
    '''Simple test to assert if folder cleanup based on prefix works'''
    d = tmp_path / "dir_to_be_deleted"
    d.mkdir()
    assert os.path.exists(d)
    result = dir.clean_up_folder_starting_with(tmp_path, "dir")
    out, err = capsys.readouterr()
    assert not os.path.exists(d)
    assert result == True
    assert err == ''

def test_clean_up_folder_starting_with_when_not_empty(tmp_path, capsys):
    '''Simple test to assert if folder cleanup based on prefix works, when directory not empty'''
    d = tmp_path / "dir_to_be_deleted"
    d.mkdir()
    os.chdir(d)
    with open('file.txt', 'w') as f:
        f.write('New file insid direcotry to be deleted!')
    assert os.path.exists(d)
    assert os.path.exists(os.path.join(d,'file.txt'))
    result = dir.clean_up_folder_starting_with(tmp_path, "dir")
    out, err = capsys.readouterr()
    assert not os.path.exists(d)
    assert result == True
    assert err == ''

def test_clean_up_folder_starting_with_when_bad_prefix(tmp_path, capsys):
    '''Simple test to assert if folder cleanup based on prefix works'''
    d = tmp_path / "dir_to_be_deleted"
    d.mkdir()
    assert os.path.exists(d)
    result = dir.clean_up_folder_starting_with(tmp_path, "bad_dir")
    out, err = capsys.readouterr()
    assert os.path.exists(d)
    assert result == True
    assert out.strip() == f"SKIP: Prefix: bad_dir not matching to any folder in directory: {tmp_path}"
    assert err == ''

def test_clean_up_folder_starting_with_when_name_equals_prefix(tmp_path, capsys):
    '''Simple test to assert if folder cleanup based on prefix works'''
    d = tmp_path / "dir_to_be_deleted"
    d.mkdir()
    assert os.path.exists(d)
    result = dir.clean_up_folder_starting_with(tmp_path, "dir_to_be_deleted")
    out, err = capsys.readouterr()
    assert not os.path.exists(d)
    assert result == True
    assert err == ''