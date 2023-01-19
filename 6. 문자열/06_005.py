a = input()
s = a.upper()
arr = sorted(set(list(s)))
lst = []

for x in arr:
    n = s.count(x)
    lst.append(n)
m = max(lst)

cnt = 0
for y in lst:
    if y == m:
        cnt += 1

if cnt == 1:
    print(arr[lst.index(m)])
else:
    print('?')



