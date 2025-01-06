# writing files
import json
import csv
txt_data = "I like Pizza"
# file_path = "output.txt"
# file_path = "/Users/jay/Desktop/o2.json"

# try:
#     with open(file_path , "x") as file:
#         file.write(txt_data)
#         print(f"txt file {file_path} created")
# except FileExistsError:
    # print(f"txt file {file_path} already exists")


# a for append, r for read, w for write ,x for create

# employees = ["jay" , "squidward" , "patrick" , "spongebob"]

# with open(file_path , "w") as file:
#     for employee in employees:
#         file.write(employee + " ")
#     print(f"file created")

# json file

# employee = {
#     "name" : "spongebob",
#     "age" : 30,
#     "job" : "manager"
# }

# with open(file_path , "w") as file:
#     json.dump(employee , file , indent=4)
#     print(f"file created")


# csv file
file_path = "/Users/jay/Desktop/o2.csv"
employees = [
    ["Name" , "Age" , "Job"],
    ["Spongebob" , 21 , "cook"],
    ["patrick" , 19 , "manager"],
    ["squidward" , 17 , "fisherman"]
]

try :
    with open(file_path , "w" , newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print("csv created")
except FileExistsError:
    print("already exists")