t1 = ('a', 'b', 'c', 'd', 'e')

t2 = tuple('lupins')
print(t2)


txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)
