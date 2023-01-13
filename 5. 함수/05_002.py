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






