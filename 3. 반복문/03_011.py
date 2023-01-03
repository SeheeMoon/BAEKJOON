while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break # 예외처리를 통해 break를 걸어주는 방법

    # sys를 사용하는 방법

# import sys
# lines = sys.stdin.readlines()
# for line in lines:
#     A, B = map(int, line.split())
#     print(A+B)