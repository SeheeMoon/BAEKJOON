N = int(input())
a = int(N/5)

while a > 0:
    if N - (5*a) == 0:
        print(a)
        break
    if (N - (5*a)) % 3 == 0:
        print(int(a + ((N - (5*a)) / 3)))
        break
    else:
        a -= 1

if a == 0:
    if N % 3 == 0:
        print(int(N / 3))
    else:
        print(-1)

    
        