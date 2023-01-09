C = int(input())
for i in range(C):
    arr = list(map(int, input().split()))
    t = 0
    avg = sum(arr[1:]) / arr[0]
    for x in arr[1:]:
        if x > avg:
            t += 1
    rate = t/arr[0] *100
    print(f'{rate:.3f}%') # f스트링을 쓸 것
