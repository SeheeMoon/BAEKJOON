T = int(input())
for i in range(T):
    sum = 0
    weight = 0
    str = list(input())
    for i in range (len(str)):
        if str[i] == 'X':
            weight = 0
        if str[i] == 'O':
            weight += 1
            sum = sum + weight
    print(sum)

