T = int(input())
for i in range (T):
    R, S = input().split()
    S = list(S)
    R = int(R)
    P = ''
    for i in range(len(S)): # S를 리스트 변환 하지 않고 for i in S: 로도 가능 (문자열도 in 의 범주가 될 수 있다.)
        P += S[i] * R
    print(P)


