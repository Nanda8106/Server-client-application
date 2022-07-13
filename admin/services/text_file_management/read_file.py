"""
This module ruturn the data from the given data by users
"""
import os
from pydoc import classname


def read_file(user_object: classname, file_name: str = None) -> str:
    """
    Returns the first hundred characters from the file provided by the user
    If the file_name is not given currently opened file will be closed
    Parameters
    ----------
    user_object: classname
        UserDetails class object which contains all the information regarding current user
    file_name : str
        file_name to read the data
    """
    current_file = user_object.get_current_file()
    directory = user_object.get_current_directory()
    # if file_name doesn't exist
    if file_name and not os.path.exists(str(f"{directory}/{file_name}")):
        return str(f"Given file name {file_name} doesn't exist in the {directory}")
    # if file_name is not given previously opened file will be closed
    if not file_name:
        if current_file == "":
            return str("No files are currently opened")
        user_object.change_current_file("")
        return str(f"Previously opened file {current_file} is closed")
    # The index and current file will be changed if the previously opened
    # file and the current file are not the same.
    if file_name and file_name != current_file:
        user_object.change_current_file(file_name)
        user_object.change_file_index(0)
    current_file = user_object.get_current_file()
    file_path = directory+"/"+current_file
    try:
        with open(file_path, "r", encoding="utf8") as read:
            data = read.read()
            if len(data) == 0:
                return str("There is no data in the file")
            initial_index = user_object.get_file_index()
            final_index = initial_index + 100
            next_hundred_character = data[initial_index: final_index]
            if final_index >= len(data):
                user_object.change_file_index(0)
            else:
                user_object.change_file_index(final_index)
            return next_hundred_character
    except FileNotFoundError:
        return str("File not exist in the current directory")
    except PermissionError:
        return str("File name must be in format. Check once before you enter commands")
    except Exception:
        return str("Something went wrong. Check your command once whether it is correct or not")
