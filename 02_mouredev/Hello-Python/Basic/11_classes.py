'''Classes_python'''
# https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# DEFINITION


class MyEmptyPerson:
    '''class person'''
    pass  # Empty class


print(MyEmptyPerson)
print(MyEmptyPerson())

# Class with Entity


class Person:
    '''class Person'''

    def __init__(self, name, surname, alias="No alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Public property.
        self.__name = name  # Private property.

    def get_name(self):
        '''get name'''
        return self.__name

    def walk(self):
        '''function walk'''
        print(f"{self.full_name} is walking.")


my_person = Person("Brown", "Michael")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brown", "Michael", "Mike")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Michael Cartoon (loves dogs)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)
