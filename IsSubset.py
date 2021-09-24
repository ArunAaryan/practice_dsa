def isSubset( a1, a2, n, m):
    d = {}
    for val in a1:
        d[val] = 1
    for val in a2:
        if val not in d:
            return False
    return True
def isSubsetSort( a1, a2, n, m):
    a1.sort()
    a2.sort()
    i = j = 0
    while i < n and j < m:
        if a1[i] < a2[j]:
            i += 1
        elif a1[i] == a2[j]:
            j += 1
            i += 1
        elif a1[i] > a2[j]:
            break
    return False if j < m else True

res = isSubsetSort([1,2,3],[2,3], 3,2)
print(res)