a, b = map(int, input().split())
c = int(input())
# if 0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 1000:
#     if b + c < 60:
#         print(a, b + c)
#     for i in range (1, 17):
#         if 60 * i <= b + c < 60 * (i + 1):
#             if a + i < 24:
#                 print(a + i, (c - (60 - b)) - 60 * (i - 1))
#             if a + i >= 24:
#                 print(a + i - 24, (c - (60 - b)) - 60 * (i - 1))

hour = (b + c)//60
min = (b + c)%60

if b + c >= 60:
    if (a + hour) >= 24:
        a = a - 24
    a = a + hour
    print(a, min)
 
else:
    if (a + hour) >= 24:
        a = a - 24
    print(a, b + c)
# 상황에 맞게 변수로 바인딩하는 것도 중요.