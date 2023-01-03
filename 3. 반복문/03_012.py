N = input()
C = 0
T = N


while True:
    if int(T) < 10:
        T = '0' + T[-1]
    T = T[-1] + str(int(T[0]) + int(T[-1]))[-1]
    C += 1
    if int(T) == int(N):
        break

print(C)





    
