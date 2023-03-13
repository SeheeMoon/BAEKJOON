A = list(input())
B = list(input())
C = list(input())
D = list(input())
E = list(input())

lst = [A, B, C, D, E]
lst_len = []
for x in lst:
    lst_len.append(len(x))

m = max(lst_len)

for x in lst:
    cnt = m
    a = cnt - len(x)
    while a > 0:
        x.append('')
        a -= 1

str = ''
for i in range(m):
    for x in lst:
        str += x[i]

print(str)
