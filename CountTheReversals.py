import math
def countTheReversals(s):
    left = right = 0
    if len(s) % 2:
        return -1
    for i in range(len(s)):
        if s[i] == '{':
            left += 1
        else:
            if not left:
                right += 1
            else:
                left -= 1
    ans = math.ceil(left / 2) + math.ceil(right / 2)
    return ans 

res = countTheReversals('}{{}}}{{')
print(res)


