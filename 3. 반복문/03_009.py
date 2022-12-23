N = int(input())
str = '*'
for i in range(1, N+1):
    print((str * i).rjust(N, ' '))