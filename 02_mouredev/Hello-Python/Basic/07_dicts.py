# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Name": "Michael",
                 "Surname": "Brown", "Age": 35, 1: "Python"}


my_dict = {
    "Name": "Michael",
    "Surname": "Brown",
    "Age": 35,
    "Languages": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Name"])
print (my_dict["Languages"])
print("Brown" in my_dict)
print("Surname" in my_dict)


# Insert

my_dict["Street"] = "Street Fish"
print(my_dict)

# Update

my_dict["Name"] = "Pedro"
print(my_dict["Name"])

# Delete

del my_dict["Street"]
print(my_dict)

# Other operations

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Name", 1, "Story"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Name", 1, "Story"))
print('fromkeys: ',(my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print('fromkeys: ',(my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Fish")
print('fromkeys: ',(my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))



#Dictionaries inside dictionaries

dictionary = {'key' : 'value',
'key_2': 'value_2'}

nested_dict = { 'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3])
