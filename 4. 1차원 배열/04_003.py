N = int(input())
N_list = list(map(int, input().split()))
lst = []
lst.append(min(N_list))
lst.append(max(N_list))
print(*lst) # print함수에 end=" "을 사용함으로써 출력 후 빈칸을 뒤에 표시하고 개행하지 못하게 출력할 수도 있다.