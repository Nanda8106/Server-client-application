"""
This module is responsible for displaying list of files in the specified directory
and their sizez, time of creation.
"""
import os
from datetime import datetime


def display_list(current_path: str) -> str:
    """
    returns the list of files, directories and their size, date of creation and time
    present in the currently working directory
    Parameters
    ----------
    current_path : str
        current working directory of user
    """
    if os.path.isdir(current_path):
        output = "filename, file_size, date and time of creation\n" \
                 "---------------------------------------------------\n"
        for file in os.scandir(current_path):
            date = datetime.fromtimestamp(file.stat().st_atime).strftime('%Y-%m-%d-%H:%M')
            output += str(f"{file.name}, {file.stat().st_size}, {date}\n")
        return output

    else:
        return str(f"directory {current_path} doesn't exists  ")
