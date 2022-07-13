"""
This module allows users to write content into the specified file and
to remove the data from the file
"""
def write_file(current_path: str, file_name: str, input_data: str = None) -> str:
    """
    append the given input data into the given file.
    If the input_data is empty data will be erased from the given file
    Parameters
    ----------
    current_path : str
        current working directory of user
    file_name: str
        file_name to write the data
    input_data: str
        data to write or append to the given file
    """
    file_path = current_path+"/"+file_name
    try:
        if input_data:
            with open(file_path, "a", encoding="utf8") as append:
                data = input_data + "\n"
                append.writelines(data)
            return str(f"Successfully written data into {file_name}")
        with open(file_path, "w", encoding="utf8") as create:
            create.truncate()
        return str(f"Successfully removed data {file_name}")
    except FileNotFoundError:
        return str(f"{file_name} not found")
    except PermissionError:
        return str("File name must be in format. Check once before you enter commands")
    except Exception:
        return str("Something went wrong. Check your command once whether it is correct or not")
