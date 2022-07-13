"""
This module allows user to login into the application
"""
import os


def singin(username: str, password: str, path: str, change_username) -> str:
    """
    Signin the user to the application, if the user already logged in returns error message
    Parameters
    ----------
    username: str
        user username
    password: str
        user password
    path : str
        Path to the data where logs.txt and credentials.txt is stored
    change_username: function
        this function changes the username after user successfully logged in
    """
    file = path+"/credentials.txt"
    if not os.path.isfile(file):
        open(file, 'w').close()
    try:
        with open(file, "r", encoding="utf8") as read:
            data = read.readlines()
            for each_user in data:
                each_user_split = list(each_user.split(","))
                exist_username = each_user_split[0]
                exist_password = (each_user_split[1]).strip()
                if password == exist_password and username == exist_username:
                    if not is_user_already_logged_in(username, path):
                        reply = log_user(username, path)
                        if reply == "Success":
                            change_username(username)
                            return "Success"
                        else:
                            return reply
                    else:
                        return str("User already logged in another server. "
                                   "Try to exit in that server.")
            else:
                return str("Wrong Credentials")
    except FileNotFoundError:
        return str("File not found. Try again")
    except Exception:
        return str("Please try again")


def log_user(username: str, path: str) -> str:
    """
    stores the user username in logs.txt file
    Parameters
    ----------
    username: str
        user username
    path : str
        Path to the data where logs.txt  stored
    """
    file = path+"/logs.txt"
    try:
        with open(file, "a", encoding="utf8") as append:
            data = f"{username}\n"
            append.writelines(data)
        return str("Success")
    except FileNotFoundError:
        return str("File not found. Try again1")


def is_user_already_logged_in(username: str, path: str) -> bool:
    """
    returns True if user already logged in another server, False if not logged in
    Parameters
    ----------
    username: str
        user username
    path : str
        Path to the data where logs.txt is stored
    """
    file = path+"/logs.txt"
    try:
        with open(file, "r", encoding="utf8") as read:
            data = read.readlines()
            for each_data in data:
                if each_data.strip() == username:
                    return True
            else:
                return False
    except FileNotFoundError:
        print("File not found. Try again")
        return False
