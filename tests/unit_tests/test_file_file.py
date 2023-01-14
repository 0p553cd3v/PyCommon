import os
from py_common.sp_file import m_file 

def test_create_new_file(tmp_path, capsys):
    '''Main path test to assert if cfile is created'''
    d = tmp_path
    os.chdir(d)
    result = m_file.create_new_file("./file.txt")
    out, err = capsys.readouterr()
    assert result == 0
    assert out.strip() == "SUCCESS: File ./file.txt created"
    assert err == ''

def test_create_new_file_when_exist(tmp_path, capsys):
    '''Alternate path test to assert if file is not created when exist'''
    d = tmp_path
    os.chdir(d)
    with open('./file.txt', 'w'):
        pass 
    result = m_file.create_new_file("./file.txt")
    out, err = capsys.readouterr()
    assert result == 0
    assert out.strip() == "SKIP: File ./file.txt already exist"
    assert err == ''

def test_create_new_file_when_folder_not_exist(capsys):
    '''Alternate path test to assert if file is not created when directory not exist'''
    result = m_file.create_new_file("./some_folder/file.txt")
    out, err = capsys.readouterr()
    assert result == 11
    assert out.strip() == "Destination folder " + os.path.dirname("./some_folder/file.txt") + " not exist"
    assert err == ''

def test_overwrite_line_with_matching_prefix_to_file(tmp_path, capsys):
    '''Main path to assert if line added when mathcing prefix found'''
    d = tmp_path
    os.chdir(d)
    with open('./file.txt', 'a') as file:
        file.write('TEST_PREFIX: Old test content')
    
    new_content = 'New test content'    
    result = m_file.overwrite_line_with_matching_prefix_to_file("./file.txt", "TEST_PREFIX: ", new_content)
    out, err = capsys.readouterr()
    assert result == 0
    assert out.strip() == "Replacing TEST_PREFIX: Old test content with TEST_PREFIX: " + new_content + "\n\nSUCCESS: Line added to file ./file.txt"
    assert err == ''

def test_overwrite_line_with_matching_prefix_to_file_when_line_exist(tmp_path, capsys):
    '''Alternative path to assert if line skipped when line already added'''
    d = tmp_path
    os.chdir(d)
    with open('./file.txt', 'a') as file:
        file.write('TEST_PREFIX: Old test content\n')
    
    new_content = 'Old test content'    
    result = m_file.overwrite_line_with_matching_prefix_to_file("./file.txt", "TEST_PREFIX: ", new_content)
    out, err = capsys.readouterr()
    assert result == 0
    assert out.strip() == "SKIP: Line TEST_PREFIX: Old test content\n already added"
    assert err == ''

def test_overwrite_line_with_matching_prefix_to_file_when_line_not_found(tmp_path, capsys):
    '''Alternative path to assert if line added when matching prefix not found'''
    d = tmp_path
    os.chdir(d)
    with open('./file.txt', 'a') as file:
        pass
    
    new_content = 'New test content'    
    result = m_file.overwrite_line_with_matching_prefix_to_file("./file.txt", "TEST_PREFIX: ", new_content)
    out, err = capsys.readouterr()
    assert result == 0
    assert out.strip() == "Adding TEST_PREFIX: " + new_content + "\n as new line\nSUCCESS: Line added to file ./file.txt"
    assert err == ''

def test_overwrite_line_with_matching_prefix_to_file_when_file_not_found(tmp_path, capsys):
    '''Alternative path to assert if error on file not found'''
    d = tmp_path
    os.chdir(d)
    
    new_content = 'New test content'    
    result = m_file.overwrite_line_with_matching_prefix_to_file("./file.txt", "TEST_PREFIX: ", new_content)
    out, err = capsys.readouterr()
    assert result == 10
    assert out.strip() == "Destination file ./file.txt not exist"
    assert err == ''