word = input()
c_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
sum = 0
for i in c_alph:
    if i in word:
        word = word.replace(i, '/')

print(len(word))
