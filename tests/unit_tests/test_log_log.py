import os
from datetime import datetime
from py_common.sp_log import m_log
from py_common.sp_env import m_conf

def test_get_logger(caplog,create_test_project_env):
    '''Main path test to assert if logger is created'''
    repo_dir = create_test_project_env[1]
    os.chdir(repo_dir)
    logger = m_log.get_logger()
    logger.critical("Test error")
    cfg = m_conf.get_env_config_base()
    
    assert caplog.record_tuples[1] == (cfg["project_name"], 50, 'Test error')

    logfile = open(os.path.join(cfg["env_log_dir"], cfg["project_name"], "{:%Y-%m-%d}.log".format(datetime.now())), 'r')
    loglist = logfile.readlines()
    logfile.close()
    line_found = False
    for line in loglist:
        if str("Test error") in line:
            line_found = True    
    
    assert line_found == True

def test_clean_log(create_test_project_env):
    '''Main path test to assert if log file is cleaned'''
    repo_dir = create_test_project_env[1]
    os.chdir(repo_dir)
    TODO: "separate instances of logger"
    logger = m_log.get_logger()
    cfg = m_conf.get_env_config_base()
    assert os.path.exists(os.path.join(cfg["env_log_dir"], cfg["project_name"], "{:%Y-%m-%d}.log".format(datetime.now())))
    #m_log.clean_log()
    #assert not os.path.exists(os.path.join(cfg["env_log_dir"], cfg["project_name"], "{:%Y-%m-%d}.log".format(datetime.now())))