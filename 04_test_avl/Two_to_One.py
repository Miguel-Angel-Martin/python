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
    """_summary_

    Args:
        a1 (_type_): first string
        a2 (_type_): second string to compare

    Returns:
        _type_: Return a new sorted string, the longest possible, containing distinct letters
    """
    result = ""
    for x in a1:
        if x not in result:
            result = result + x
    for x in a2:
        if x not in result:
            result = result + x
    return ''.join(sorted(result))

# def longest(s1, s2):
#     return ''.join(sorted((set(s1+s2))))


a = "xyaabbbccccdef"
b = "xxxxyyyyabklmopq"
print(longest(a, b))
