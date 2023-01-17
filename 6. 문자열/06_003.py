S = list(map(str, input()))
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for x in lst:
    if x in S:
        print(S.index(x), end=' ')
    else:
        print(-1, end=' ')

 # 아스키 코드를 활용하여 알파벳 리스트를 쉽게 찾을 수 있다 +) find함수가 문제에서 요구하는 그대로임

# s = input()
# for i in range(97,123):
#     print(s.find(chr(i)), end=' ')