"""Script runners module."""

# Imports
import sys
import os
import subprocess

from py_common.sp_base import m_print
from py_common.sp_log import m_log

# from py_common.sp_env import m_conf


def run_subprocess_check_call(name: str, description: str, command: str, subprocess_run_dir="", subprocess_repo_dir=""):
    """Run subprocess check call with defined parameters and logging.

    Args:
        name (str): Name of the function to be run (one word)
        description (str): Descriptipon to be added (3-4 words)
        command (cmd): Command to be rune in fomr of an array

    Returns:
        int: Error number
    """
    base_run_dir = os.getcwd()

    if subprocess_repo_dir != "":
        os.chdir(os.path.abspath(subprocess_repo_dir))

    # Start logger instance
    logger = m_log.get_logger()
    # cfg = m_conf.get_env_conf_all()

    logger.debug(f"Script runned from: {base_run_dir}")

    logger.debug(f"Subprocess repo dir: {os.getcwd()}")

    if subprocess_run_dir != "":
        os.chdir(os.path.abspath(subprocess_run_dir))
    else:
        # For scenario when run dir not specified but script was runned from diffrrent directory then repo dir
        os.chdir(os.path.abspath(base_run_dir))

    logger.debug(f"Subprocess run dir: {os.getcwd()}")

    # Print separator
    m_print.print_line_separator_with_title(name + " - " + description, "-", 100)

    logger.info(f"{name} run started")

    try:
        subprocess.check_call(command, shell=False)
    except subprocess.CalledProcessError as e:
        logger.exception(f"{name} run failed: {e}")
        sys.exit(1)
    else:
        logger.info(f"{name} run finished - SUCCESS")
        # Returning to script run dir
        os.chdir(os.path.abspath(base_run_dir))
        return 0
