non_self = []
for n in range(1,10001):
    def d(n):
        sum = 0
        for i in range(len(str(n))):
            sum += int(str(n)[i])
        n += sum
        non_self.append(n)
    nself = list(set(non_self))
    d(n)

lst = []
for i in range(1,10001):
    lst.append(i)

lst_sub_non_self = [x for x in lst if x not in non_self]

for x in lst_sub_non_self:
    print(x)

# natural_num = set(range(1,10001))
# generated_num = set()

# for i in range(1, 10001):
#     for j in str(i): # ex) i = 850, for문에서 str도 범위로 설정될 수 있구나.
#         i += int(j)  # ex) 850 + 8 + 5 + 0 = 863
#     generated_num.add(i)

# self_num = sorted(natural_num - generated_num) # set은 차집합을 구할 수 있음.
# for i in self_num:
#     print(i)






