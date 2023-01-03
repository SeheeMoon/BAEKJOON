lstA = []
lstB = []
T = 0
while True:
    A, B = map(int, input().split())
    lstA.append(A)
    lstB.append(B)
    T += 1
    if A == 0 and B == 0:
        for i in range(T-1):
            print(lstA[i] + lstB[i])
        break

# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)