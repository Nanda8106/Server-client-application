"""
This function allows user signup into the application with username
and password
"""
import os
from . import sign_in


def signup(username: str, password: str, path: str, change_username) -> str:
    """
    Signup the new user to the application and create folder for the user, if the username
    already exist returns error message
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
        with open(file, "w", encoding="utf8") as write:
            data = f"{username},{password}\n"
            write.writelines(data)
        sign_in.singin(username, password, path, change_username)
        users_path = os.path.dirname(os.getcwd())+"/users"
        reply = create_folder(users_path, username)
        if reply == "Success":
            return "Success"
        else:
            return reply
    try:
        is_user_exist = False
        with open(file, "r", encoding="utf8") as read:
            data = read.readlines()
            for each_user in data:
                user_details_split = list(each_user.split(","))
                exist_username = user_details_split[0]
                if exist_username == username:
                    is_user_exist = True
                    break
        if not is_user_exist:
            with open(file, "a", encoding="utf8") as append:
                data = f"{username},{password}\n"
                append.writelines(data)
            sign_in.singin(username, password, path, change_username)
            users_path = os.path.dirname(os.getcwd())+"/users"
            reply = create_folder(users_path, username)
            if reply == "Success":
                return "Success"
            else:
                return reply
        return str("User already exist with the username. Try with other username!")
    except FileNotFoundError:
        return str("Try again")


def create_folder(path: str, folder_name: str) -> str:
    """
    create the folder with the given name in the given directory
    Parameters
    ----------
    path : str
        path upto to users folder
    folder_name: str
        folder name to create in the current directory
    """
    new_path = path+"/"+folder_name
    if not os.path.exists(new_path):
        try:
            os.makedirs(new_path)
            return str("Success")
        except Exception:
            return str("Try once again")
