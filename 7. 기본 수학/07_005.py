T = int(input())
lst = []
for i in range(T):
    H, W, N = map(int, input().split())
    a = N % H
    if a == 0:
        a = H
    b = (N-1) // H + 1
    if b < 10:
        b = '0' + str(b)
    print(str(a) + str(b))


