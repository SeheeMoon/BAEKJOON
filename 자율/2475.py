a = input().split()
num = 0
for x in a:
    t = int(x) ** 2
    num += t
print(num%10)


