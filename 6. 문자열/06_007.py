a, b = input().split()
A = int("".join(list(reversed(a))))
B = int("".join(list(reversed(b))))
if A > B:
    print(A)
elif B > A:
    print(B)
