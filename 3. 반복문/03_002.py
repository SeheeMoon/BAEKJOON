T = int(input())
lstA = []
lstB = []
for i in range(0, T):
    A, B = map(int, input().split())
    lstA.append(A)
    lstB.append(B)
for i in range(0, T):
    print(lstA[i]+lstB[i])