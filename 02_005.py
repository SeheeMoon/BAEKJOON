H, M = map(int, input().split())
if M >= 45:
    print(H, M - 45)
if H == 0 and M < 45:
    print(23, M + 15)
elif M < 45:
    print(H - 1, M + 15)