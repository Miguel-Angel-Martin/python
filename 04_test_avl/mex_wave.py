'''
https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python

The wave (known as the Mexican wave in the English-speaking world outside North America)

wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
'''


def wave(words):
    result = []
    chars = list(words)
    print(chars)
    for index, char in enumerate(chars):
        if char.isalpha():
            copy = chars[:]
            copy[index] = copy[index].upper()
            print("sol:", copy)
            result.append(''.join(copy))
    return result


print(wave("hello"))

# def wave(str):
#     return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
