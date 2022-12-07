'''
    https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
    There is an array with some numbers. All numbers are equal except for one. Try to find it!

    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
'''


def find_uniq(array):
    '''find_uniq _summary_

    Args:
        array (_type_): _description_
    '''
    result = 0
    for item in array:
        if array.count(item) == 1:
            result = item
    return result


array = [1, 1, 1, 2, 3, 1]
print(find_uniq(array))
