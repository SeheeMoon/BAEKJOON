a = list(map(int, input().split()))
lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [8, 7, 6, 5, 4, 3, 2, 1]
if a == lst1:
    print('ascending')
elif a == lst2:
    print('descending')
else:
    print('mixed') # 굳이 리스트로 안 만들어도 input().split()만으로 비교가 가능하고, 문자열로도 비교가 가능함.
    # sorted 함수 사용해도 .. 좋다