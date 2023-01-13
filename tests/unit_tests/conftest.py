import pytest
import os

@pytest.fixture()
def create_test_project_env(tmp_path, autouse=True):
    test_home = tmp_path
    test_project_name = "TestProject"
    test_log_level = "INFO"
    test_env_log_dir = os.path.join(test_home, ".log")
    test_env_dcv_dir = os.path.join(test_home, "docker-volumes")
    test_env_conf_dir = os.path.join(test_home, ".config")
    test_log_dir = os.path.join(test_env_log_dir, test_project_name)
    test_repo_dir = os.path.join(test_home, test_project_name)
    test_conf_repo_dir = os.path.join(test_repo_dir, "config")
    os.chdir(test_home)
    os.makedirs(test_log_dir)
    os.makedirs(test_conf_repo_dir)

    with open(os.path.join(test_conf_repo_dir, "env.yml"), 'a') as file:
        file.write('PROJECT_NAME: ' + test_project_name + "\n")
        file.write('ENV_LOG_DIR: ' + test_env_log_dir + "\n")
        file.write('ENV_CONF_DIR: ' + test_env_conf_dir + "\n")
        file.write('ENV_DCV_DIR: ' + test_env_dcv_dir + "\n")
        file.write('LOG_LEVEL: ' + test_log_level + "\n")
    return [ test_home, test_repo_dir, test_log_dir]