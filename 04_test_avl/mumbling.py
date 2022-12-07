'''
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
This time no story, no theory. The examples below show you how to write function accum:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''


def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


print(accum("abc"))
