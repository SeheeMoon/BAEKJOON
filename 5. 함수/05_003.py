N = int(input())
lst = []
for i in range(1, N+1):
    if i // 10 <= 9:
        lst.append(i)
    if i // 10 >= 10:
        a = str(i)
        if int(a[1]) == (int(a[0]) + int(a[2])) / 2: # N < 1000 이기 때문에 등차중항을 이용함.
            lst.append(i)

print(len(lst))

# num_list[0]-num_list[1] == num_list[1]-num_list[2] 요렇게 간단하게도 표현 가능하구나