'''file handling'''
# https://youtu.be/TbcEqkabAWU?t=15524

### File Handling ###

import xml
import csv
import json
import os

# .txt file

# Read, write and update if the file exist
txt_file = open("02_mouredev/Hello-Python/Intermediate/my_file.txt", "w+")

txt_file.write(
    "My name is Miguel\nMi surname is Martin\nI'm 44 years old\nAnd my favorite language is Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAlthough I like very much JS")
print(txt_file.readline())

txt_file.close()

with open("02_mouredev/Hello-Python/Intermediate/my_file.txt", "a") as my_other_file:
     my_other_file.write("\nY C#")

# os.remove("Intermediate/my_file.txt")

# # Clase en vídeo (03/11/22): https://www.twitch.tv/videos/1642512950

# # .json file


# json_file = open("/02_mouredev/Hello-Python/Intermediate/my_file.json", "w+")

# json_test = {
#     "name": "Brais",
#     "surname": "Moure",
#     "age": 35,
#     "languages": ["Python", "Swift", "Kotlin"],
#     "website": "https://moure.dev"}

# json.dump(json_test, json_file, indent=2)

# json_file.close()

# with open("/02_mouredev/Hello-Python/Intermediate/my_file.json") as my_other_file:
#     for line in my_other_file.readlines():
#         print(line)

# json_dict = json.load(
#     open("/02_mouredev/Hello-Python/Intermediate/my_file.json"))
# print(json_dict)
# print(type(json_dict))
# print(json_dict["name"])

# # .csv file


# csv_file = open("/02_mouredev/Hello-Python/Intermediate/my_file.csv", "w+")

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["name", "surname", "age", "language", "website"])
# csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
# csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

# csv_file.close()

# with open("/02_mouredev/Hello-Python/Intermediate/my_file.csv") as my_other_file:
#     for line in my_other_file.readlines():
#         print(line)

# # .xlsx file
# # import xlrd # Debe instalarse el módulo

# # .xml file

# # ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?
