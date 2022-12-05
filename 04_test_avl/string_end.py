
'''
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string). 

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

'''

def solution(string, ending):
    '''solution _summary_

    Args:
        string (_type_): string for test
        ending (_type_): string to search at the end of the string
    '''

    return string.endswith(ending)

s1= "abcdefg"
s2="ghjk"
print(solution(s1, s2))