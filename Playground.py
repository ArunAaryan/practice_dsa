from itertools import cycle
string  = 'abcd'
c = cycle(string) 

res = []
for i in range(len(string)):
    st = ''
    count = 0 
    for j in (c):
        if count == len(string):
            break
        st += j
        count += 1
    res.append(st)
    res.append(st[::-1])
res = set(res)
print(len(res))

