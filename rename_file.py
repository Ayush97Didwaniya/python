import os
def rename_files():
       file_list = os.listdir(r"F:\udacity\python programs\rename_file\prank")
       print(file_list)
       saved_path = os.getcwd()
       print("current working directory"+saved_path)
       os.chdir(r"F:\udacity\python programs\rename_file\prank")
       for file_name in file_list:
           os.rename(file_name, file_name.translate(None,"0123456789"))
       os.chdir(saved_path)
rename_files()
