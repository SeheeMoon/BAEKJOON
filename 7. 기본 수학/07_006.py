T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())

    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    for i in range(k):
        for j in range(13):
            lst[j+1] = lst[j] + lst[j+1]
    
    print(lst[n-1])
            

    # def people_num(k, n):
    #     if k == 0:
    #         return n
    #     if n == 0:
    #         return 0
    #     else:
    #         result = people_num(k, n-1) + people_num(k-1, n)
    #         return result
    
    # print(people_num(k, n))