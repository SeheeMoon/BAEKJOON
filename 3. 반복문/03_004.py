X = int(input())
N = int(input())
total = 0
for i in range(0, N):
    a, b = map(int, input().split())
    total += (a * b)
if X == total:
    print('Yes')
else:
    print('No')