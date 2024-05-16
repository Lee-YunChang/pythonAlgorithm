croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = str(input())

for i in croatia:
    word = word.replace(i, '_')

print((len(word)))

