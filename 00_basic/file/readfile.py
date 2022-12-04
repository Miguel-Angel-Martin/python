fhand = open('file/mbox.txt')

count = 0
''' for line in fhand:
    count = count + 1
print('Line Count:', count) '''

for line in fhand:
    if line.startswith('From:'):
        print(line)