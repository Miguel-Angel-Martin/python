'''
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
'''


def spin_words(sentence):
    words = sentence.split()
    countOfWords = " "
    for index, x in enumerate(words):
        if len(x) >= 5:
            x = x[::-1]
            words[index] = x
    return (countOfWords.join(words))


print(spin_words("test counter words"))
