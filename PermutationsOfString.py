from itertools import permutations

def permutationsOfString(string):
    string = sorted(list(string))
    res = []
    p = permutations(range(len(string)))
    for i in p:
        tmp = ''
        for j in i:
            tmp += string[j]
        res.append(tmp)
    return res
res = permutationsOfString('BCA')
print(res)
