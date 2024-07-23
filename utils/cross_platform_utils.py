# cross_platform_utils.py

import os
import platform

def get_platform_info() -> str:
    """
    Get information about the current platform.
    """
    return platform.system() + " " + platform.version()

def ensure_directory_exists(path: str) -> None:
    """
    Ensure that a directory exists; create it if it does not.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def read_file_cross_platform(file_path: str) -> str:
    """
    Read a file in a cross-platform manner.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    return content
