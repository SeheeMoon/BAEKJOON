X = int(input())
i = 1
j = 1

while True: # 분자
    if X == 1:
        a = 1
        break
    if 2*i**2-i+1 <= X <= 2*i**2+3*i+1:
        c = X - (2*i**2-i+1)
        lst1 = []
        for x in range(1, 2*i+1 + 1):
            lst1.append(x)
        for x in range(2*i, 0, -1):
            lst1.append(x)
        a = lst1[c]
        break
    else:
        i += 1

while True: # 분모
    if 2*j**2-3*j+2 <= X <= 2*j**2+j:
        d = X - (2*j**2-3*j+2)
        lst2 = []
        for x in range(1, 2*j + 1):
            lst2.append(x)
        for x in range(2*j-1, 0, -1):
            lst2.append(x)
        b = lst2[d]
        break
    else:
        j += 1

print(f'{a}/{b}')
