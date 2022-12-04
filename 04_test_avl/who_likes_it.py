'''
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

'''


def likes(names):
    result = " "
    people = " "
    persons = 0
    if len(names) == 0:
        result = "no one likes this"
    else:
        for index, name in enumerate(names):
            if index <= 2:
                if index == len(names)-1 and len(names) > 1:
                    people = people + " and "
                else:
                    if index != 0:
                        people = people + ", "
                people = people + name
            else:
                persons += 1

        if persons != 0:
            result = people + " and " + str(persons) + " others like this"
        else:
            if len(names) == 1:
                result = people + " likes this"
            else:
                result = people + " like this"

    return (result.strip())


names =['Alex', 'Jacob', 'Mark', 'Max']
print(likes(names))
