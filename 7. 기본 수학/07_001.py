A, B, C = map(int, input().split())
try:
    x = int(A / (C - B))
    if C - B < 0:
        print(-1)
    else:
        print(x + 1)
except ZeroDivisionError:
    print(-1)