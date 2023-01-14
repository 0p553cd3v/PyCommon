"""Logger module."""

# Imports
import os
import logging
import sys
import inspect
from datetime import datetime
from py_common.sp_env import m_conf


def clean_log():
    """Clean todays log file for project

    Returns:
        int: Return error number
    """
    cfg = m_conf.get_env_config_base()

    log_path = os.path.join(cfg["env_log_dir"], cfg["project_name"], "{:%Y-%m-%d}.log".format(datetime.now()))

    # Remove log file
    os.remove(log_path)
    return 0


def get_logger():
    """Get logger instance for whole project.

    Returns:
        logger: Returns initialize logger with name equal to {projectname}
    """
    # Get name of the script that runned get_logger function
    script_name = os.path.basename(inspect.getsourcefile(sys._getframe(1))).replace(".py", "")

    # Get configuration
    cfg = m_conf.get_env_config_base()

    # Set logger instance
    logger = logging.getLogger(cfg["project_name"])
    logger.setLevel(cfg["log_level"])
    if not logger.handlers:
        # Configure console "print" handler
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(cfg["log_level"])
        consoleFormatter = logging.Formatter("%(levelname)s : " + script_name + " : %(funcName)s : %(message)s")
        consoleHandler.setFormatter(consoleFormatter)
        logger.addHandler(consoleHandler)

        # Create directory to store logs
        os.makedirs(os.path.join(cfg["env_log_dir"], cfg["project_name"]), exist_ok=True)
        # Configure file handler
        fileHandler = logging.FileHandler(
            os.path.join(cfg["env_log_dir"], cfg["project_name"], "{:%Y-%m-%d}.log".format(datetime.now())), mode="a"
        )
        fileHandler.setLevel(cfg["log_level"])
        fileFormatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : " + script_name + " : %(funcName)s : %(message)s",
            datefmt="%d-%m-%Y %I:%M:%S",
        )
        fileHandler.setFormatter(fileFormatter)
        logger.addHandler(fileHandler)

        logger.info(f"New logger initialized for project: {cfg['project_name']}")

        # Return configured logger instance
    return logger
