N = int(input())
arr = list(map(int, input().split()))
m = max(arr)
lst = []
for x in arr:
    a = x / m * 100
    lst.append(a)

n = sum(lst)/len(lst)
print(n)
