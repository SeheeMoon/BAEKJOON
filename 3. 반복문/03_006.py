T = int(input())
lst = []
for i in range(1, T + 1):
    A, B = map(int, input().split())
    lst.append(A + B)
for i in range(0, T):
    print('Case #' + str(i+1) + ':', lst[i])
