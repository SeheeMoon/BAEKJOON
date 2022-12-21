# a, b, c = map(int, input().split())
# if a == b and a == c:
#     print(10000 + a * 1000)
# elif a == b and a != c:
#     print(1000 + b * 100)
# elif a != b and a == c:
#     print(1000 + c * 100)
# elif a != b and b == c:
#     print(1000 + c * 100)
# elif a != b and a != c and b != c:
#     if a > b > c or a > c > b:
#         print(a * 100)
#     elif b > a > c or b > c > a:
#         print(b * 100)
#     elif c > b > a or c > a > b:
#         print(c * 100)

a,b,c=map(int,input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b or b==c:
    print(1000+b*100)
elif a==c:
    print(1000+a*100)
else:
    print(max(a,b,c)*100) 

# 연산자 두개 연속으로 써도 되고, max 함수는 최댓값을 반환하는 함수이다.