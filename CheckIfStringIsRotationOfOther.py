def checkIfStringIsRotationOfOther(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1 * 2
    first = second = 0
    while first < len(s1) and s1[first]!= s2[second]:
        first += 1
    if first == len(s1):
        return False
    while first < len(s1) and second < len(s2):
        if s1[first] != s2[second]:
            return False
        first += 1
        second += 1
    return True

res =  checkIfStringIsRotationOfOther('abcd','dabc')
print(res)
