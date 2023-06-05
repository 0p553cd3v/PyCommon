import pytest
import os
import subprocess

@pytest.fixture()
def create_test_project_env(tmp_path, autouse=True):
    test_home = tmp_path
    test_project_name = "TestProject"
    test_log_level = "INFO"
    test_env_log_dir = os.path.join(test_home, ".log")
    test_env_dcv_dir = os.path.join(test_home, "docker-volumes")
    test_env_conf_dir = os.path.join(test_home, ".config")
    test_env_keys_dir = os.path.join(test_home, ".keys")
    test_log_dir = os.path.join(test_env_log_dir, test_project_name)
    test_conf_dir = os.path.join(test_env_conf_dir, test_project_name)
    test_keys_dir = os.path.join(test_env_keys_dir, test_project_name)
    test_repo_dir = os.path.join(test_home, test_project_name)
    test_conf_repo_dir = os.path.join(test_repo_dir, "config")
    os.chdir(test_home)
    os.makedirs(test_log_dir)
    os.makedirs(test_conf_repo_dir)
    os.makedirs(test_conf_dir)
    os.makedirs(test_keys_dir)

    with open(os.path.join(test_conf_repo_dir, "env.yml"), 'a') as file:
        file.write('PROJECT_NAME: ' + test_project_name + "\n")
        file.write('ENV_LOG_DIR: ' + test_env_log_dir + "\n")
        file.write('ENV_CONF_DIR: ' + test_env_conf_dir + "\n")
        file.write('ENV_DCV_DIR: ' + test_env_dcv_dir + "\n")
        file.write('ENV_KEYS_DIR: ' + test_env_keys_dir + "\n")
        file.write('LOG_LEVEL: ' + test_log_level + "\n")
    return [ test_home, test_repo_dir, test_log_dir]

@pytest.fixture(scope="session", autouse=True)
def build_dummy_docker_image(tmp_path_factory):
    tmpdir = tmp_path_factory.mktemp("data")
    os.chdir(tmpdir)
    print(tmpdir)
    health_check_content = (
        f"import sys\n"
        f"import os\n"
        f"if os.path.isfile('if_i_exist_the_container_is_healthy.txt'):\n"
        f"    sys.exit(0)\n"
        f"print('Health check failed!!!')\n"
        f"sys.exit(1)\n"
        )

    print(health_check_content)

    with open("health-check.py", "w") as f_hc:
        f_hc.write(health_check_content)

    i_exist_content = (
        "I exist!!!\n"
        )

    print(i_exist_content)

    with open("if_i_exist_the_container_is_healthy.txt", "w") as f_ih:
        f_ih.write(i_exist_content)

    dockerfile_content = (
        f"FROM python:3.9\n"
        f"WORKDIR /home\n"
        f"COPY . .\n"
        f"RUN chmod +x health-check.py\n"
        f"HEALTHCHECK --interval=5s --timeout=3s CMD python health-check.py\n"
        f'ENTRYPOINT ["tail", "-f", "/dev/null"]\n'
        )

    print(dockerfile_content)

    with open("Dockerfile", "w") as f_dc:
        f_dc.write(dockerfile_content)

    build_command = "docker build --no-cache -t dummy_docker_image ."
    subprocess.call(['bash', '-c', build_command])
    