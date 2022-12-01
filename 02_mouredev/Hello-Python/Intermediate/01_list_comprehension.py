'''list'''
#  https://youtu.be/TbcEqkabAWU?t=3239

### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print("Original:", my_original_list)

my_range = range(8)
print("Range:", list(my_range))

# Definition

my_list = [i + 1 for i in range(8)]
print("Range + 1:", my_list)

my_list = [i * 2 for i in range(8)]
print('Range i*2: ', my_list)

my_list = [i * i for i in range(8)]
print('Range i*i: ', my_list)


def sum_five(number):
    '''add five to a some number'''
    return number + 5


my_list = [sum_five(i) for i in range(8)]
print("Function add 5:", my_list)
