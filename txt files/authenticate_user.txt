"""
This module calls respctive authentication related services based on command
given by the user
"""
from .entry.sign_up import signup
from .entry.sign_in import singin


def authenticate(cmd: str, path: str, change_username) -> dict:
    """
    based on the given commands calls the particular service for authentication
    Parameters
    ----------
    cmd: str
        user command
    path : str
        Path to the data where logs.txt and credentials.txt is stored
    change_username: function
        this function changes the username after user successfully logged in
    """
    cmd_split = list(cmd.split())
    reply = {}
    if cmd_split[0] == "login":
        if len(cmd_split) == 3:
            username = cmd_split[1]
            password = cmd_split[2]
            reply_signin = singin(username.lower(), password, path, change_username)
            if reply_signin == "Success":
                reply = format_reply(True, "You are successfully logged in!")
            else:
                reply = format_reply(False, reply_signin)
        else:
            reply = format_reply(
                False,
                "command is incomplete. Enter correct command to authenticate"
            )
    elif cmd_split[0] == "register":
        if len(cmd_split) == 3:
            username = cmd_split[1]
            password = cmd_split[2]
            reply_signup = signup(username.lower(), password, path, change_username)
            if reply_signup == "Success":
                reply =  format_reply(
                    True,
                    "User account created successfully. You are now logged in!"
                )
            else:
                reply =  format_reply(False, reply_signup)
        else:
            reply =  format_reply(
                False,
                "command is incomplete. Enter correct command to authenticate"
            )
    else:
        reply = format_reply(
            False,
            "command is incorrect. Enter correct command to authenticate"
        )
    return reply


def format_reply(is_success: bool, message: str) -> dict:
    """
    reformat the reply came from other modules
    Parameters
    ----------
    is_success: bool
        True or False
    message: str
        message to format
    """
    reply = {}
    if not is_success:
        reply["status"] = "Fail"
    else:
        reply["status"] = "Success"
    reply["message"] = message
    return reply
