import os
from datetime import datetime
from py_common.sp_script import m_run
from py_common.sp_env import m_conf 

def test_run_subprocess_check_call(capsys,create_test_project_env, caplog):
    '''Main path test on running command'''
    #Finding build path based on build.py script location
    test_repo_dir = create_test_project_env[1]
    os.chdir(test_repo_dir)
    cfg = m_conf.get_env_config_base()  
    test_dir = os.path.join(test_repo_dir, "test_path")
    os.mkdir(test_dir)
    os.chdir(test_repo_dir)
    result = m_run.run_subprocess_check_call("Touch", "Create file", ["touch", "test_file.txt"], test_dir, test_repo_dir)
    #Assert commandHandler
    out, err = capsys.readouterr()
    assert os.getcwd() == test_dir
    assert out.strip() == "----------------------------------------Touch - Create file-----------------------------------------"
    assert os.path.exists(os.path.join(test_dir,"test_file.txt"))
    assert result == 0

    INFO_MESSAGE = "Touch run started"
        
    assert caplog.record_tuples[1] == (cfg["project_name"], 20, INFO_MESSAGE)

    logfile = open(os.path.join(cfg["env_log_dir"], cfg["project_name"], "{:%Y-%m-%d}.log".format(datetime.now())), 'r')
    loglist = logfile.readlines()
    logfile.close()
    line_found = False
    for line in loglist:
        if str(INFO_MESSAGE) in line:
            line_found = True    
    
    assert line_found == True
