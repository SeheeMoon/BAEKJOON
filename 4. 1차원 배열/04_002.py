N, X = map(int, input().split())
A = list(map(int, input().split()))
lst = []
for x in A:
    if x < X:
        lst.append(x)

print(*lst) # 리스트 요소 한번에 출력하기

