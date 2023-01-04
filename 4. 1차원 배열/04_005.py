lst1 = []
for i in range(1, 31):
    lst1.append(i)

lst2 = []
for i in range(28):
    a = int(input())
    lst2.append(a)
    
for i in lst1:
    if i not in lst2:
        print(i)
