'''
https://www.codewars.com/kata/554b4ac871d6813a03000035/python
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
'''


# def high_and_low(numbers):
#     l = list(numbers.split())
#     l = [int(i) for i in l]
#     high = max(l)
#     low = min(l)
#     result = str(str(high)+" " + str(low))
#     return result

def high_and_low(numbers):  # z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn), min(nn))


print(high_and_low("1 2 3 4 5"))
