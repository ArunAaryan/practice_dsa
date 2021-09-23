import collections #type this
def minWindow( s, t):
    if not s or not t:
        return ''

    #from here to her
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]
    # till here
res = minWindow('My Name is Fran','rim')
print(res)
res = minWindow('I am the greatest','Imt')
print(res)

# iput1


