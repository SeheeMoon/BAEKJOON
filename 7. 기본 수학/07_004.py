A, B, V = map(int, input().split())

d = (V - A) / (A - B) 
if int(d) < d:
    print(int(d) + 2)
else:
    print(int(d) + 1)

