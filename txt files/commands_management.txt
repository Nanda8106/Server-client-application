"""
Module to calls respective services based on the command given by users
"""
from pydoc import classname
from .directory_management.create_folder import create_folder
from .directory_management.change_folder import change_folder
from .text_file_management.write_file import write_file
from .text_file_management.read_file import read_file
from .directory_management.list import display_list
from .print_commands import return_commands


def call_commands(cmd: str, user_object: classname) -> str:
    """
    calls the respective services based on the provided command
    Parameters
    ----------
    cmd : str
        command for specific task
    user_object: classname
        UserDetails class object which contains all the information regarding current user
    """
    split_cmd = list(cmd.split(" ", 2))
    if len(split_cmd) >= 1:
        if split_cmd[0] == "create_folder":
            if len(split_cmd) == 2:
                reply = create_folder(
                    split_cmd[1], user_object.get_current_directory())
                return reply
            return str("Incorrect command")
        elif split_cmd[0] == "change_folder":
            if len(split_cmd) == 2:
                reply = change_folder(split_cmd[1], user_object)
                return reply
            return str("Incorrect command")
        elif split_cmd[0] == "read_file":
            if len(split_cmd) == 1:
                reply = read_file(user_object)
            elif len(split_cmd) == 2:
                reply = read_file(user_object, split_cmd[1])
            else:
                reply = str("Incorrect command")
            return reply
        elif split_cmd[0] == "write_file":
            if len(split_cmd) == 3:
                reply = write_file(
                    user_object.get_current_directory(), split_cmd[1], split_cmd[2])
            elif len(split_cmd) == 2:
                reply = write_file(
                    user_object.get_current_directory(), split_cmd[1])
            else:
                reply = str("Incorrect command")
            return reply

        elif split_cmd[0] == "commands":
            if len(split_cmd) == 1:
                path = user_object.get_root() + "/data"
                reply = return_commands(path)
            else:
                reply = str("Incorrect command")
            return reply
        elif split_cmd[0] == "list":
            if len(split_cmd) == 1:
                reply = display_list(user_object.get_current_directory())
            else:
                reply = str("Incorrect command")
            return reply
        else:
            return str("Incorrect command")
    else:
        return str("Incorrect command")
