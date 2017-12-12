import os
import re
def rename_files():
    file_list = os.listdir(r"/Users/bryon/Udacity Python Intro/prank")

    saved_path = os.getcwd()
    os.chdir(r"/Users/bryon/Udacity Python Intro/prank")
    for file_name in file_list:
        os.rename(file_name, re.sub('[0-9]','',file_name))
    os.chdir(saved_path)
        
rename_files()
