"""Script runners module."""

# Imports
import sys
import subprocess

from py_common.base import prints
from py_common.log import log


def run_subprocess_check_call(name, description, command):
    """_summary_

    Args:
        name (str): Name of the function to be run (one word)
        description (str): Descriptipon to be added (3-4 words)
        command (cmd): Command to be rune in fomr of an array

    Returns:
        int: Error number
    """
    # Start logger instance
    logger = log.get_logger()

    # Print separator
    prints.print_line_separator_with_title(name + " - " + description, "-", 100)

    logger.info(f"{name} run started")

    try:
        subprocess.check_call(command, shell=False)
    except subprocess.CalledProcessError as e:
        logger.error(f"{name} run failed: {e.returncode}")
        sys.exit(1)
    else:
        logger.info("{name} run finished - SUCCESS")
        return 0
