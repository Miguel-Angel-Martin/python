'''Error types'''
# https://youtu.be/TbcEqkabAWU?t=12721

### Error Types ###

# SyntaxError
# print "¡Hola comunidad!" # DesComment to force an  Error
from math import pi
import math
print("¡Hello community!")

# NameError
language = "Spanish"  # Comment to force an  Error
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # DesComment to force an  Error

# ModuleNotFoundError
# import maths # DesComment to force an  Error

# AttributeError
# print(math.PI) # DesComment to force an  Error
print(math.pi)

# KeyError
my_dict = {"Name": "Michael", "Surname": "Martin", "Age": 35, 1: "Python"}
print(my_dict["Age"])
# print(my_dict["Surname"]) # DesComment to force an  Error
print(my_dict["Surname"])

# TypeError
# print(my_list["0"]) # DesComment to force an  Error
print(my_list[0])
print(my_list[False])

# ImportError
# from math import PI # DesComment to force an  Error
print(pi)

# ValueError
#my_int = int("10 years")
my_int = int("10")  # DesComment to force an  Error
print(type(my_int))

# ZeroDivisionError
# print(4/0) # DesComment to force an  Error
print(4/2)
