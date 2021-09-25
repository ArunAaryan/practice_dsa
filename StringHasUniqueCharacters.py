def stringHasUniqueCharacters(s):
    def getValue(c):
        return ord(c)-ord('z')
    isPresent = [0] * 26
    for c in s:
        value = getValue(c)
        if isPresent[value]:
            return False
        isPresent[value] = 1
    return True
res = stringHasUniqueCharacters('abcas')
print(res)

