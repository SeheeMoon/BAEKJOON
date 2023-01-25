N = int(input())
lst = []
sum = 0

for i in range(N):
    word = input()
    lst.append(word)

for i in lst:
    lst1 = []
    for j in i:
        indices = [i for i, c in enumerate(i) if c == j]
        if indices not in lst1:
            lst1.append(indices)  

    cnt = 0        
    for k in lst1:
        if len(i) > 1:
            for l in range(len(k) - 1):
                if k[l+1] - k[l] != 1:
                    cnt += 1

    if cnt == 0:
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
