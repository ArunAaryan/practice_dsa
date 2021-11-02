def checkPalindromeFromIndex(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] == string[right]:
            left -= 1
            right += 1
        else:
            break
    return string[left + 1 : right]


def longestPalindromeInAString(string):
    max_res = ""
    for i in range(len(string)):
        res = checkPalindromeFromIndex(string, i, i)
        if len(res) > len(max_res):
            max_res = res
        
        res = checkPalindromeFromIndex(string, i, i + 1)
        if len(res) > len(max_res):
            max_res = res
    return max_res

res = longestPalindromeInAString('ababac')
print(res)