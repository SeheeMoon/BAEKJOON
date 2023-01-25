N = int(input())
lst = []
sum = 0

for i in range(N):
    word = input()
    lst.append(word)

for i in lst: # 입력한 단어들에 대하여
    lst1 = []
    for j in i: # 단어들의 알파벳에 대하여
        indices = [i for i, c in enumerate(i) if c == j] # 해당 알파벳의 인덱스 모두를 리스트로 만들어 바인딩
        if indices not in lst1: # 알파벳 당 인덱스 리스트는 하나만 
            lst1.append(indices)  # 새로운 리스트에 알파벳 인덱스 리스트를 추가

    cnt = 0        
    for k in lst1: # 각각의 알파벳 인덱스 리스트에 대하여
        if len(i) > 1: # 알파벳이 하나 이상일 때
            for l in range(len(k) - 1):
                if k[l+1] - k[l] != 1: # 인덱스가 연속되지 않을 경우 (인덱스값의 차이가 1이 아닌 경우)
                    cnt += 1 # cnt값을 추가한다.

    if cnt == 0: # cnt값이 하나라도 추가되지 않을 경우 (인덱스가 모두 연속할 경우))
        sum += 1 

print(sum)

# import sys
# input = sys.stdin.readline

# cnt = 0
# for i in range(int(input())):
#     word = input()
#     if list(word) == sorted(word, key=word.find):
#         cnt += 1
# print(cnt)
