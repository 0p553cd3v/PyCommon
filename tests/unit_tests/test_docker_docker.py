import subprocess
from docker.models.containers import Container
import docker
from py_common.sp_docker import m_docker

def test_container_name():
    '''Main path test to assert if container is retrived corectly'''
    #subprocess.check_call("docker kill hello-world")
    subprocess.check_call("docker run hello-world")
    container = m_docker.get_container_by_name("hello-world")
    assert type(container) is Container

def test_get_container_health():
    '''Main path test to assert if container health is retirived properly'''
    #subprocess.check_call("docker kill hello-world")
    subprocess.check_call("docker run hello-world")
    result = m_docker.get_container_health(m_docker.get_container_by_name("hello-world"))
    assert (result == "starting" or result == "healthy")

def test_wait_for_container_to_be_up_and_running():
    '''Main path test to assert if custom separator print function prints separator'''
    #subprocess.check_call("docker kill hello-world")
    subprocess.check_call("docker run hello-world")
    m_docker.wait_for_docker_container_up_and_running(m_docker.get_container_by_name("hello-world"),1)
    result = m_docker.get_container_health(m_docker.get_container_by_name("hello-world"))
    assert result == "healthy"

