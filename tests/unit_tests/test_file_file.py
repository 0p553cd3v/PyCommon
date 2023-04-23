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

def test_copy_new_file_to_dir(tmp_path, capsys):
    '''Main path test to assert if file was copied'''
    d = tmp_path
    os.chdir(d)
    source_file_path=os.path.join(d, "file.txt")
    with open(source_file_path, "x"):
        pass
    dest_dir = os.path.join(d, "dest_folder")
    os.mkdir(dest_dir)
    result = m_file.copy_new_file_to_dir(source_file_path, dest_dir)
    assert os.path.exists(os.path.join(dest_dir,"file.txt"))
    out, err = capsys.readouterr()
    assert result == 0
    assert out.strip() == f"SUCCESS: File {source_file_path} added to directory {dest_dir}"
    assert err == ''

def test_copy_new_file_to_dir_when_exist(tmp_path, capsys):
    '''Alternative path test to assert if file was not copied when exist'''
    d = tmp_path
    os.chdir(d)
    source_file_path=os.path.join(d, "file.txt")
    dest_dir = os.path.join(d, "dest_folder")
    with open(source_file_path, "x"):
        pass
    os.mkdir(dest_dir)
    with open(os.path.join(dest_dir,"file.txt"), "x"):
        pass

    result = m_file.copy_new_file_to_dir(source_file_path, dest_dir)
    assert os.path.exists(os.path.join(dest_dir,"file.txt"))
    out, err = capsys.readouterr()
    assert result == 0
    assert out.strip() == f"SKIP: File {source_file_path} already exist in directory {dest_dir}"
    assert err == ''

def test_copy_new_file_to_dir_when_source_not_exist(tmp_path, capsys):
    '''Alternative path test to assert if error when source file not exist'''
    d = tmp_path
    os.chdir(d)
    source_file_path=os.path.join(d, "file.txt")
    dest_dir = os.path.join(d, "dest_folder")
    os.mkdir(dest_dir)
    result = m_file.copy_new_file_to_dir(source_file_path, dest_dir)
    out, err = capsys.readouterr()
    assert result == 2
    assert out.strip() == f"File {source_file_path} not exist"
    assert err == ''

def test_copy_new_file_to_dir_when_dest_dir_not_exist(tmp_path, capsys):
    '''Alternative path test to assert if file was not copied when direcotry not exist'''
    d = tmp_path
    os.chdir(d)
    source_file_path=os.path.join(d, "file.txt")
    with open(source_file_path, "x"):
        pass
    dest_dir = os.path.join(d, "dest_folder")
    result = m_file.copy_new_file_to_dir(source_file_path, dest_dir)
    out, err = capsys.readouterr()
    assert result == 1
    assert out.strip() == f"Folder {dest_dir} not exist"
    assert err == ''


def test_write_content_to_empty_file(tmp_path, capsys):
    '''Main path to assert if content added if file is empty'''
    d = tmp_path
    os.chdir(d)
    with open('./file.txt', 'a') as file:
        file.write('')
    
    new_content = [
        'New test content - line 1',
        'New test content - line 2',
    ]  

    result = m_file.write_content_to_empty_file("./file.txt", new_content)
    out, err = capsys.readouterr()
    assert result == 0
    assert out.strip() == "SUCCESS: Content added to file ./file.txt"
    assert err == ''

def test_write_content_to_empty_file_when_file_not_found(tmp_path, capsys):
    '''Alternative path to assert if error on file not found'''
    d = tmp_path
    os.chdir(d)
    
    new_content = [
        'New test content - line 1',
        'New test content - line 2',
    ]  

    result = m_file.write_content_to_empty_file("./file.txt", new_content)
    out, err = capsys.readouterr()
    assert result == 10
    assert out.strip() == "Destination file ./file.txt not exist"
    assert err == ''

def test_write_content_to_empty_file_when_not_empty(tmp_path, capsys):
    '''Alternative path to assert if error on file not empty'''
    d = tmp_path
    os.chdir(d)
    
    with open('./file.txt', 'a') as file:
        file.write('Some not expected content')
    
    new_content = [
        'New test content - line 1',
        'New test content - line 2',
    ]  

    result = m_file.write_content_to_empty_file("./file.txt", new_content)
    out, err = capsys.readouterr()
    assert result == 20
    assert out.strip() == "Destination file ./file.txt is not empty"
    assert err == ''