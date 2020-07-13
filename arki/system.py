import os
import sys


def is_linux():
    """
    Check if the current platform is Linux.
    :return: True if the current platform is Linux; False otherwise
    """
    return sys.platform.startswith("linux")


def is_windows():
    """
    Check if the current platform is Windows.
    :return: True if the current platform is Windows; False otherwise
    """
    return sys.platform.startswith("win")


def run_command(command):
    """
    Run a command
    :param command: command string
    :return: return code (0 means all good)
    """
    print(command)
    ret_code = os.system(command)

    print(f"Command return code: {ret_code}")
    return ret_code
