def solve(a):
    ans = 0
    for x in a:
        ans += x
    return ans

while True:
    try:
        a = list(map(int, input().split()))
        solve(a)
    except EOFError:
        break

# def solve(a):
#   return sum(a) 이렇게 구현 가능..
