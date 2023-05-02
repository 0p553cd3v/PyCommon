import subprocess
from docker.models.containers import Container
import docker
import os
from py_common.sp_docker import m_docker
import pytest

WAIT_EXECUTION_TIMEOUT = 60

def test_container_name():
    '''Main path test to assert if container is retrived corectly'''
    CONTAINER_NAME = "test_container_name"
    IMAGE_NAME = "dummy_docker_image"
    subprocess.check_call(
        [
            "docker",
            "run",
            "-d",
            "-t",
            "--name",
            CONTAINER_NAME,
            IMAGE_NAME,
        ]
    )
    container = m_docker.get_container_by_name(CONTAINER_NAME)
    subprocess.check_call(
        [
            "docker",
            "rm",
            "-f",
            CONTAINER_NAME,
        ]
    )
    assert type(container) is Container

def test_get_container_health():
    '''Main path test to assert if container health is retirived properly'''
    CONTAINER_NAME = "test_get_container_health"
    IMAGE_NAME = "dummy_docker_image"
    
    subprocess.check_call(
        [
            "docker",
            "run",
            "-d",
            "-t",
            "--name",
            CONTAINER_NAME,
            IMAGE_NAME,
        ]
    )
    result = m_docker.get_container_health(m_docker.get_container_by_name(CONTAINER_NAME))
    subprocess.check_call(
        [
            "docker",
            "rm",
            "-f",
            CONTAINER_NAME,
        ]
    )
    
    assert (result == "starting" or result == "healthy")

def test_stop_all_docker_containers():
    '''Main path test to assert if all running containers are stoped.'''
    CONTAINER_NAME_1 = "test_stop_all_docker_containers_1"
    CONTAINER_NAME_2 = "test_stop_all_docker_containers_2"
    IMAGE_NAME = "dummy_docker_image"

    #Clean up conteiners before test
    subprocess.check_call(
        [
            "docker",
            "rm",
            "-f",
            "$(docker",
            "ps",
            "-a",
            "-q)",
        ], 
        shell=True
    )

    #Run first container
    subprocess.check_call(
        [
            "docker",
            "run",
            "-d",
            "-t",
            "--name",
            CONTAINER_NAME_1,
            IMAGE_NAME,
        ]
    )

    #Run second container
    subprocess.check_call(
        [
            "docker",
            "run",
            "-d",
            "-t",
            "--name",
            CONTAINER_NAME_2,
            IMAGE_NAME,
        ]
    )

    ps_run = subprocess.check_output('docker ps', shell=True)
    ps_run_found = False
    if ps_run.find(CONTAINER_NAME_1) != -1 and ps_run.find(CONTAINER_NAME_2) != -1:
        ps_run_found = True
    assert ps_run_found == True

    result = m_docker.stop_all_docker_containers()

    ps_stop = subprocess.check_output('docker ps', shell=True)

    ps_stop_not_found = False
    if ps_stop.find(CONTAINER_NAME_1) == -1 and ps_stop.find(CONTAINER_NAME_2) == -1:
        ps_stop_not_found = True
    assert ps_stop_not_found == True

    #Cleanup of stoped docker images
    subprocess.check_call(
        [
            "docker",
            "rm",
            "-f",
            "$(docker",
            "ps",
            "-a",
            "-q)",
        ], 
        shell=True
    )

    assert result == 0

def test_stop_all_docker_containers_when_no_containers_running(capsys):
    '''Alternative path test to assert if recoginzed when no containers are running.'''

    #Clean up conteiners before test
    subprocess.check_call(
        [
            "docker",
            "rm",
            "-f",
            "$(docker",
            "ps",
            "-a",
            "-q)",
        ], 
        shell=True
    )

    result = m_docker.stop_all_docker_containers()
    out, err = capsys.readouterr()
    print(out)
    assert result == 0
    assert out.strip() == "SKIP: No running containers."
    assert err == ''

@pytest.mark.execution_timeout(WAIT_EXECUTION_TIMEOUT)
def test_wait_for_container_to_be_up_and_running():
    '''Main path test to assert if function waits for container to be up and running'''
    CONTAINER_NAME = "test_wait_for_container_to_be_up_and_running"
    IMAGE_NAME = "dummy_docker_image"
    subprocess.check_call(
        [
            "docker",
            "run",
            "-d",
            "-t",
            "--name",
            CONTAINER_NAME,
            IMAGE_NAME,
        ]
    )
    m_docker.wait_for_docker_container_up_and_running(m_docker.get_container_by_name(CONTAINER_NAME),1)
    result = m_docker.get_container_health(m_docker.get_container_by_name(CONTAINER_NAME))
    subprocess.check_call(
        [
            "docker",
            "rm",
            "-f",
            CONTAINER_NAME,
        ]
    )
    assert result == "healthy"