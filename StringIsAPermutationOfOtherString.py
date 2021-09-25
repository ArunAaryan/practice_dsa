def stringPermutationOfOther(s1, s2):
    def getValue(c):
        return ord(c) - ord('a')
    arr = [0] * 128
    for i in s1:
        val = getValue(i)
        arr[val] += 1
    for i in s2:
        val = getValue(i)
        arr[val] -= 1
        if arr[val] < 0:
            return False
    return True

res = stringPermutationOfOther('avaadsf','sfda')
print(res)
