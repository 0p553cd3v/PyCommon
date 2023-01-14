import os
from datetime import datetime
from py_common.sp_log import m_log
from py_common.sp_env import m_conf

def test_get_logger_and_clean_log(caplog,create_test_project_env):
    '''Main path test to assert if logger is created and then log file is deleted'''
    TEST_ERROR_MESSAGE = "Unit test sample critical error"
    test_repo_dir = create_test_project_env[1]
    os.chdir(test_repo_dir)
    logger = m_log.get_logger()
    logger.critical(TEST_ERROR_MESSAGE)
    cfg = m_conf.get_env_config_base()
    
    assert caplog.record_tuples[1] == (cfg["project_name"], 50, TEST_ERROR_MESSAGE)

    logfile = open(os.path.join(cfg["env_log_dir"], cfg["project_name"], "{:%Y-%m-%d}.log".format(datetime.now())), 'r')
    loglist = logfile.readlines()
    logfile.close()
    line_found = False
    for line in loglist:
        if str(TEST_ERROR_MESSAGE) in line:
            line_found = True    
    
    assert line_found == True

    assert os.path.exists(os.path.join(cfg["env_log_dir"], cfg["project_name"], "{:%Y-%m-%d}.log".format(datetime.now())))
    m_log.clean_log()
    assert not os.path.exists(os.path.join(cfg["env_log_dir"], cfg["project_name"], "{:%Y-%m-%d}.log".format(datetime.now())))

