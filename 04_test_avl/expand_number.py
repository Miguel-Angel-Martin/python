'''
https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

'''


def expanded_form(num):
    result = []
    divider = 10
    while divider < num:
        temp = num % divider
        print(temp)
        print(divider)
        if temp != 0:
            result.insert(0, str(temp))
        num -= temp
        divider *= 10
    result.insert(0, str(num))
    return '+'.join(result)


print(expanded_form(1210))
