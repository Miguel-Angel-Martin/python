'''
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
'''
import string


def alphabet_position(text):
    letters = [*text]
    result = []
    alphabet = list(string.ascii_lowercase)
    for letter in letters:
        if letter.lower() in alphabet:
            result.append(alphabet.index(letter.lower())+1)
    return result


print(alphabet_position("The sunset sets at twelve o' clock."))
