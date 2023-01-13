N = int(input())
lst = []
for i in range(1, N+1):
    if i // 10 <= 9:
        lst.append(i)
    if i // 10 >= 10:
        a = str(i)
        if int(a[1]) == (int(a[0]) + int(a[2])) / 2:
            lst.append(i)

print(len(lst))