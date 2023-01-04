lst = []
for i in range(9):
    a = int(input())
    lst.append(a)

n = max(lst)
i = int(lst.index(n)) + 1
print(n)
print(i)
