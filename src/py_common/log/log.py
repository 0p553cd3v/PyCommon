"""Logger module."""

# Imports
import os
import logging
import sys
import inspect
from datetime import datetime
import yaml


def _get_logger_config():
    """Get parameters from config file.

    Returns:
        [str,str,str]: Returning project name, environemnt logging directory and defined log level
    """
    # Read env.yaml to get project parameters
    with open(os.path.join("config", "env.yml"), "r") as file:
        ENV = yaml.safe_load(file)

    # Read necessary parameters
    PROJECT_NAME = ENV["PROJECT_NAME"]
    ENV_LOG_DIR = os.path.expanduser(ENV["ENV_LOG_DIR"])
    LOG_LEVEL = ENV["LOG_LEVEL"]

    # Return necessary parameters
    return PROJECT_NAME, ENV_LOG_DIR, LOG_LEVEL


def clean_log():
    """Clean todays log file for project

    Returns:
        int: Return error number
    """
    # Read env.yaml to get project parameters
    with open(os.path.join("config", "env.yml"), "r") as file:
        ENV = yaml.safe_load(file)

    # Read necessary parameters
    PROJECT_NAME = ENV["PROJECT_NAME"]
    ENV_LOG_DIR = os.path.expanduser(ENV["ENV_LOG_DIR"])
    log_path = os.path.join(ENV_LOG_DIR, PROJECT_NAME, "{:%Y-%m-%d}.log".format(datetime.now()))

    # Remove log file
    if os.path.isfile(log_path):
        os.rmdir(log_path)
        return 0
    else:
        return 1


def get_logger():
    """Get logger instance for whole project.

    Args:
        projectname (str): Project name derived from config (common for all scripts within the project)
        envlogdir (str): Environment logging directory (common for all scripts and projects)
        loglevel (str): Log level from range: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
    Returns:
        logger: Returns initialize logger with name equal to {projectname}
    """
    # Get name of the script that runned get_logger function
    script_name = os.path.basename(inspect.getsourcefile(sys._getframe(1))).replace(".py", "")

    # Get configuration
    projectname, envlogdir, loglevel = _get_logger_config()

    # Set logger instance
    logger = logging.getLogger(projectname)
    logger.setLevel(loglevel)
    if not logger.handlers:
        # Configure console "print" handler
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(loglevel)
        consoleFormatter = logging.Formatter("%(levelname)s : " + script_name + " : %(funcName)s : %(message)s")
        consoleHandler.setFormatter(consoleFormatter)
        logger.addHandler(consoleHandler)

        # Create directory to store logs
        os.makedirs(os.path.join(envlogdir, projectname), exist_ok=True)
        # Configure file handler
        fileHandler = logging.FileHandler(
            os.path.join(envlogdir, projectname, "{:%Y-%m-%d}.log".format(datetime.now())), mode="a"
        )
        fileHandler.setLevel(loglevel)
        fileFormatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : " + script_name + " : %(funcName)s : %(message)s",
            datefmt="%d-%m-%Y %I:%M:%S",
        )
        fileHandler.setFormatter(fileFormatter)
        logger.addHandler(fileHandler)

        logger.info(f"New logger initialized for project: {projectname}")

        # Return configured logger instance
    return logger
