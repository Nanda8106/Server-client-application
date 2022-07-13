import unittest
import os
from services.text_file_management.write_file import write_file
from user_details import UserDetails
from services.directory_management.create_folder import create_folder
from services.directory_management.change_folder import change_folder


class TestServerClient(unittest.TestCase):
    """
    This class tests write_file, change_folder, create_folder modules
    Methods
    -------
    test_write_file(username)
        test write_file module with some random file names and input data
    test_change_folder()
        Test change folder module with random directories
    test_create_folder()
        Tests create_folder module with random folder names it contains existing folder names
    """
    def test_write_file(self):
        """
        test write_file module with some random file names and input data
        """
        user = UserDetails()
        username = "nanda"
        user.change_username(username)
        file_name = ["nanda.txt", "kishore.txt", "om.txt"]
        input_data = ["appending data", None, "This is om"]  
        exp_out = [
            f"Successfully written data into {file_name[0]}",
            f"Successfully removed data {file_name[1]}",
            f"Successfully written data into {file_name[2]}"
        ]
        result = []
        for each_test in range(3):
            result.append(write_file(
                user.get_current_directory(),
                file_name[each_test], 
                input_data=input_data[each_test]
            ))
        self.assertListEqual(result, exp_out)
        
    def test_change_folder(self):
        """
        Test change folder module with random directories
        """
        user = UserDetails()
        username = "nanda"
        user.change_username(username)
        folder_name = ["nanda", "om"]
        exp_out = []
        for index in range(2):
            path = user.get_current_directory()+"/"+folder_name[index]
            if os.path.isdir(path):
                exp_out.append(f"Directory changed to {path}")
            else:
                exp_out.append("Folder doesn't exist")
        result = []
        for each_test in range(2):
            result.append(change_folder(folder_name[each_test], user))
        self.assertListEqual(result, exp_out)
    
    def test_create_folder(self):
        """
        Tests create_folder module with random folder names it contains existing folder names
        """
        user = UserDetails()
        username = "nanda"
        user.change_username(username)
        folder_name = ["new1", "nanda"] 
        exp_out = []
        for index in range(2):
            path = user.get_current_directory()+"/"+folder_name[index]
            if os.path.isdir(path):
                exp_out.append("folder already exist in this directory")
            else:
                exp_out.append("Success")
        result = []
        for each_test in range(2):
            path = user.get_current_directory()
            result.append(create_folder(folder_name[each_test], path))
        self.assertListEqual(result, exp_out)

if __name__ == '__main__':
    unittest.main()
    print(os.getcwd())
