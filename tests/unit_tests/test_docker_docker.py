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

@pytest.mark.execution_timeout(WAIT_EXECUTION_TIMEOUT)
def test_wait_for_container_to_be_up_and_running():
    '''Main path test to assert if custom separator print function prints separator'''
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

