arr = [list(map(int, input().split())) for _ in range(9)]
m_arr = [0]
n = 1

for i in arr:
    if max(i) > max(m_arr):
        del m_arr[0:]
        m_arr.append(max(i))

        a = n
        b = i.index(max(i)) + 1

    if max(i) == max(m_arr):
        m_arr.append(max(i))
        a = n
        b = i.index(max(i)) + 1

    n += 1

print(max(m_arr))
print(a, b)

