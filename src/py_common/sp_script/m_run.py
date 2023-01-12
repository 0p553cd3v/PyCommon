"""Script runners module."""

# Imports
import sys
import subprocess

from py_common.sp_base import m_print
from py_common.sp_log import m_log

# from py_common.sp_env import m_conf


def run_subprocess_check_call(name: str, description: str, command: str):
    """_summary_

    Args:
        name (str): Name of the function to be run (one word)
        description (str): Descriptipon to be added (3-4 words)
        command (cmd): Command to be rune in fomr of an array

    Returns:
        int: Error number
    """
    # Start logger instance
    logger = m_log.get_logger()
    # cfg = m_conf.get_env_conf_all()

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
        return 0
