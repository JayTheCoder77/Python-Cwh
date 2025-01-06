# reading files in python
import json
import csv

# file_path = "/Users/jay/Desktop/output.txt"

# try:
#     with open(file_path , "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("file was not found")
# except PermissionError:
#     print("no permission to read the file")


# json

# file_path = "/Users/jay/Desktop/o2.json"

# try:
#     with open(file_path , "r") as file:
#         content = json.load(file)
#         print(content["job"])
#         print(content)
# except FileNotFoundError:
#     print("file was not found")
# except PermissionError:
#     print("no permission to read the file")

# csv

file_path = "/Users/jay/Desktop/o2.csv"

try:
    with open(file_path , "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[1])
        print(content)
except FileNotFoundError:
    print("file was not found")
except PermissionError:
    print("no permission to read the file")
