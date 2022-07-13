"""
This module logout's the user from the application
"""
def signout(logs_path: str, username: str) -> str:
    """
    Signout the user from the application and removes user logs from logs.txt file
    Parameters
    ----------
    logs_path : str
        Path of the logs.txt file where all the logged users info stored
    username: str
        user username
    """
    path = logs_path+"/data/logs.txt"
    try:
        with open(path, "r", encoding="utf8") as read:
            data = read.readlines()
        with open(path, "w") as write:
            for each_data in data:
                if each_data.strip() != username:
                    write.writelines(each_data)
            return str("User signed out successfully")
    except FileNotFoundError:
        return str("logs.txt file is missing. Try to create logs.txt in /admin/data. "
                   "or download the application once again.")
    except Exception as error:
        return str(f"Something went wrong, error: {error}")
