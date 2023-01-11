import os
from py_common.sp_path import m_path 

def test_parent_path():
    '''Main path test to assert if parent path function is generating parent path from path'''
    parent_path = "/var"
    dir = "log"
    summary_path = os.path.join(parent_path, dir)
    result = m_path.parent_path(summary_path)
    assert result == parent_path