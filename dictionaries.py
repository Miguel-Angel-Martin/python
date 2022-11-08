# list
names = ['Ana', 'John', 'Denise', 'Katy']
grade = ['B', 'A+', 'A', 'A']
course = [2.00, 6.0001, 20.002, 9.01]

# dictonaries
grades = {'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A'}
print(grades.keys())
print(grades.values())


def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


def fib_efficient(n, d):
    if n in d:
        #print("First:")
        return (d[n])
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        print (ans)
        d[n] = ans
        return ans
    
d = {1:1, 2:2}
print("Result: ",fib_efficient(6, d))