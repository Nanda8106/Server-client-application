"""
Module gives information regarding commands
"""
import os


def return_commands(path: str) -> str:
    """
    Return all the information about commands that this application accepts from user
    Parameters
    ----------
    path : str
        path upto the commands.txt file location
    """
    file = path + "/commands.txt"
    if os.path.exists(file):
        with open(file, "r", encoding="utf8") as read:
            data = read.read()
            return data

    else:
        return str("commands.txt file deleted, download the application once again.")
