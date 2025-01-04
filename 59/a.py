# py file detection

import os


file_path = "stuff/test.txt"
file_path1 = "/Users/jay/Desktop/t1.txt"
file_path2 = "/Users/jay/Desktop/test"

if os.path.exists(file_path):
    print(f"Test file exists the location is {file_path}")
else:
    print("Test file does not exist in the location")

if os.path.isfile(file_path1):
    print(f"Test file is a file in {file_path1}")
else:
    print("Test file does not exist in the location")

if os.path.isdir(file_path2):
    print(f"Test file is a folder/dir in {file_path2}")
else:
    print("Test folder/dir does not exist in the location")