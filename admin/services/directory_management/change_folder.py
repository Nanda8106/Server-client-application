"""
This module changes user directory to the mentioned directory
"""
import os
from pydoc import classname


def change_folder(folder_name: str, user_object: classname) -> str:
    """
    change the current working directory. If the folder doesn't exist returns error message
    it can't move the user from user working directory.
    Parameters
    ----------
    folder_name: str
        folder name to create in the current directory
    user_object : classname
        UserDetails class object which contains all the information regarding current user
    """
    current_directory = user_object.get_current_directory()
    user_directory = user_object.get_user_directory()
    if folder_name == "..":
        if current_directory == user_directory:
            return str("Access denied: You are currently in your root directory.")
        slash_index = current_directory.rfind("/")
        new_path = current_directory[:slash_index]
        user_object.change_curent_directory(new_path)
        return str(f"Moved back to {new_path}")
    else:
        new_path = current_directory+"/"+folder_name
        if os.path.isdir(new_path):
            user_object.change_curent_directory(new_path)
            return str(f"Directory changed to {new_path}")
        else:
            return str("Folder doesn't exist")
