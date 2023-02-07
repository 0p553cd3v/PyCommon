"""Docker configuration module."""

# Imports
from time import sleep
from docker import APIClient
from docker.models.containers import Container
import docker


def get_container_health(container: Container):
    """Get container health status.

    Args:
        container (Container): Input container type

    Returns:
        str: Returning State Health and Status of a container
    """
    api_client = APIClient()
    inspect_results = api_client.inspect_container(container.name)
    return inspect_results["State"]["Health"]["Status"]


def wait_for_docker_container_up_and_running(container: Container, time_stamp: int):
    """Wait for container to be up and running after its creation.

    Args:
        container (Container): Input container type
        time_stamp (int): Time in seconds between checks
    """
    while get_container_health(container) != "healthy":
        print(get_container_health(container))
        sleep(time_stamp)


def get_container_by_name(name: str):
    """Get instance of a container.

    Args:
        name (str): Name of the container to get its instance

    Returns:
        container: Output of container type
    """
    client = docker.from_env()
    container = client.containers.get(name)
    return container
