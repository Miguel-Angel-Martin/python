'''
https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

'''


def longest(a1, a2):
    '''longest string '''
    result = ""
    if len(a1) > len(a2):
        result = a1
    else:
        result = a2
    return result


a = "xyaabbbccccdef"
b = "xxxxyyyyabklmopq"
print(longest(a, b))
