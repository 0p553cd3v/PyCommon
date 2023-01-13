import os
import yaml
from py_common.sp_env import m_conf

def test_get_env_config_base():
    '''Main path test to assert if config is readed from base file'''
    file_dir = os.path.dirname(__file__)
    repo_dir = os.path.abspath(os.path.join(file_dir, os.pardir,os.pardir))
    os.chdir(repo_dir)
    with open(os.path.join("config", "env.yml"), "r") as file:
        f = yaml.safe_load(file)
    result = m_conf.get_env_config_base()
    assert result['project_name'] == f["PROJECT_NAME"]

def test_generate_env_config_paths():
    '''Main path test to assert if path config is generated'''
    file_dir = os.path.dirname(__file__)
    repo_dir = os.path.abspath(os.path.join(file_dir, os.pardir,os.pardir))
    os.chdir(repo_dir)
    cfg = m_conf.get_env_config_base()
    result = m_conf.generate_env_config_paths()
    with open(os.path.join(cfg["env_conf_dir"], cfg["project_name"], "paths.yml"), "r") as file:
        f = yaml.safe_load(file)
    assert repo_dir == f["REPO_DIR"]
    assert result == 0

def test_get_env_config_paths():
    '''Main path test to assert if paths are created based on config file'''
    file_dir = os.path.dirname(__file__)
    repo_dir = os.path.abspath(os.path.join(file_dir, os.pardir,os.pardir))
    os.chdir(repo_dir)
    result = m_conf.get_env_config_paths()
    assert repo_dir == result['repo_dir']

def test_get_env_conf_all():
    '''Main path test to assert if paths and config file records are created and readed'''
    file_dir = os.path.dirname(__file__)
    repo_dir = os.path.abspath(os.path.join(file_dir, os.pardir,os.pardir))
    os.chdir(repo_dir)
    with open(os.path.join("config", "env.yml"), "r") as file:
        f = yaml.safe_load(file)
    result = m_conf.get_env_conf_all()
    assert repo_dir == result['repo_dir']
    assert result['project_name'] == f["PROJECT_NAME"]