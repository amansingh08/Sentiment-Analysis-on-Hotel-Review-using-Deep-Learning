'''
Class
'''
import  os
class simulatorApp:
    def __init__(self,
                 use_local_data:bool=False):
        if use_local_data:
            return print('I am in this loop !')
        else:
            return print('I am in this False Loop !')

import os
class MarriageFolder:
    def __init__(self, folder_path):
        self.folder_path = folder_path
    def count_folders_and_files(self):
        total_folders = 0
        total_files = 0
        # Change directory to the 'marriage' folder
        os.chdir(self.folder_path)
        # List all folders and files in 'marriage'
        for item in os.listdir():
            if os.path.isdir(item):
                total_folders += 1
                file_count = len(os.listdir(item))
                total_files += file_count
                print(f"Folder: {item}, Total Files: {file_count}")
                print(f"Total Folders: {total_folders}")
                print(f"Total Files: {total_files}")
                # Specify the path to your 'marriage' folder

folder_path = r"D:/work"
marriage_folder = MarriageFolder(folder_path)
marriage_folder.count_folders_and_files()

# df = simulatorApp(use_local_data=False)
# print(df)