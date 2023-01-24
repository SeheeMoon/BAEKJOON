A = list(input())
lst = []
for i in range(65, 91):
    lst.append(chr(i))
sum = 0
for x in A:
    if x in lst[:3]:
        sum += 3
    elif x in lst[3:6]:
        sum += 4
    elif x in lst[6:9]:
        sum += 5
    elif x in lst[9:12]:
        sum += 6
    elif x in lst[12:15]:
        sum += 7
    elif x in lst[15:19]:
        sum += 8
    elif x in lst[19:22]:
        sum += 9
    elif x in lst[22:26]:
        sum += 10

print(sum)

