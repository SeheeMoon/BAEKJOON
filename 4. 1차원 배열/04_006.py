lst = []
for i in range(10):
    N = int(input())
    lst.append(N % 42)
s = set(lst)
print(len(s))

