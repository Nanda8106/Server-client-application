"""
This module allows users to create folder in specific directory
"""
import os
import re


def create_folder(folder_name: str, path: str) -> str:
    """
    create the folder with the given name in the current working directory
    Parameters
    ----------
    folder_name: str
        folder name to create in the current directory
    path : str
        current working directory of user
    """
    # regular expression for all special characters
    regexp = re.compile('[.,@!#$%^&*()<>?/|}{~:]')
    # returns error message if the folder name contains any special characters
    if regexp.search(folder_name):
        return str("Don't include these characters .,@!#$%^&*()<>?/|}{~: in folder name")
    new_path = path + "/" + folder_name
    if os.path.isdir(new_path):
        return str("folder already exist in this directory")
    else:
        try:
            os.makedirs(new_path)
            return str("Success")
        except Exception:
            return str("Something went wrong. Try again")
