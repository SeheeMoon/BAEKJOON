N = int(input())

c = 2
i = 1

while True:
    if N == 1:
        print(1)
        break
    if 3*i**2 - 3*i + 2 <= N <= 3*i**2 + 3*i + 1:
        print(c)
        break
    else:
        c += 1
        i += 1
# for c in range(19000):
#     # 계차수열의 합
#     b_list1 = []
#     for n in range(c):
#         b_list1.append(6 * (n + 1))

#     b_list2 = []
#     for n in range(c):
#         b_list2.append(6 * (n + 1) + 6)

#     sum_b1 = sum(b_list1)
#     a = 2 + sum_b1
#     sum_b2 = sum(b_list2)
#     b = 7 + sum_b2

#     if N == 1:
#         print(1)
#         break

#     elif a <= N <= b:
#         print(c + 2)
#         break