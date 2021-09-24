def findLongestConseqSubseq(arr, N):
    s = set()
    for element in arr:
        s.add(element)
    ans = 0
    for element in arr:
        if element - 1 not in s: # this is the sequence start
            ele = element
            while ele in s:
                ele += 1
            ans = max(ans, ele - element)
    return ans
res = findLongestConseqSubseq([2,6,1,9,4,5,3], 7)
print(res)
