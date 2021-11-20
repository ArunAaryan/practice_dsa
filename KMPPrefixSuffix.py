def longestPrefixSuffix(s):
    n = len(s)
    for length in range(n // 2, 0, -1): # since it starts checking from 
        # the max length it takes care of the matching short string
        prefix = s[0 : length]
        suffix = s[n - length : n] 
        if prefix == suffix :
            return length, prefix

res = longestPrefixSuffix('abcab')
print(res)