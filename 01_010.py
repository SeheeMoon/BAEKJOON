# A, B = input().split()
# a = int(A)
# b = int(B[2])
# c = int(B[1])
# d = int(B[0])
# e = int(B)
# print(a * b, a * c, a * d, a * e, sep='\n')

import sys
a = int(sys.stdin.readline().rstrip())
b = sys.stdin.readline().rstrip()
c = list(b)
print(a * int(c[2]), a * int(c[1]), a * int(c[0]), a * int(b), sep='\n')
