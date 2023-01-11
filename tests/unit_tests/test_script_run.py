import os
from py_common.sp_script import m_run 

def test_run_subprocess_check_call(capsys):
    '''Main path test on running command'''
    text_to_print = "-- Text --"
    print("OK")
    print(os.getcwd())

    result = m_run.run_subprocess_check_call("Print", "Print text", ["print("+text_to_print+")"])
    #Assert commandHandler
    out, err = capsys.readouterr()
    assert out.strip() == "-- Text --"
    assert result == 0
    print("OK")