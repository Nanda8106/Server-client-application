"""
This module is responsible for storing user details, whenever user connects with
client an instance will be created.
"""
import os


class UserDetails:
    """
    This class stores and returns all the user information like
    Attributes
    ----------
    username : str
        user username
    root_directory : str
        directory to the admin
    user_directory : str
        directory to the user folder where all the user services are done
    current_user_directory : str
        user current working will be stored in this directory
    current_file : str
        If the user opened any it will be stored in this variable
    current_file_index : int
        It will store the index of the pointer until which user read data
    -------   
    Methods
    -------
    change_username(username)
        It will change username of user
    get_username()
        returns the username of user
    get_root()
        returns the root directory
    get_user_directory()
        return the user directory
    get_current_directory()
        return the user current working directory
    change_curent_directory(path)
        change the user current directory
    change_current_file(file_name)
        replace the past file_name with the current opened file_name
    change_file_index(index)
        change the current opened file reading pointer
    get_current_file()
        returns the current opened file
    get_file_index()
        returns the current opened file index pointer
    """
    def __init__(self) -> None:
        self.username = ""
        self.root_directory = os.getcwd()
        self.user_directory = os.path.dirname(os.getcwd())+"/users"
        self.current_user_directory = self.user_directory
        self.current_file = ""
        self.current_file_index = 0

    def change_username(self, username: str) -> None:
        """
        This function change the username after the user authenticate successfully and change
        the directories
        Parameters
        ----------
        username : str
            username of user
        """
        self.username = username
        self.user_directory = self.user_directory + "/" + username
        self.current_user_directory = self.user_directory

    def get_username(self) -> str:
        """
        This function returns the username
        """
        return self.username

    def get_root(self) -> str:
        """
        This function returns the root directory
        """
        return self.root_directory

    def get_user_directory(self) -> str:
        """
        This function returns the user root directory
        """
        return self.user_directory

    def get_current_directory(self) -> str:
        """
        This function return the user current working directory
        """
        return self.current_user_directory

    def change_curent_directory(self, path: str) -> None:
        """
        This function changes the user current working directory
        Parameters
        ----------
        path : str
            user current working directory
        """
        self.current_user_directory = path

    def change_current_file(self, file_name: str) -> None:
        """
        This function replace the user current reading file
        Parameters
        ----------
        file_name : str
        """
        self.current_file = file_name

    def change_file_index(self, index: int) -> None:
        """
        This function change the current file reading pointer position
        Parameters
        ----------
        index : int
            current opened file pointer position
        """
        self.current_file_index = index

    def get_current_file(self) -> str:
        """
        This function returns the current opened file
        """
        return self.current_file

    def get_file_index(self) -> int:
        """
        This function returns the current opened file pointer position
        """
        return self.current_file_index
