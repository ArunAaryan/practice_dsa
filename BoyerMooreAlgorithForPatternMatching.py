from collections import defaultdict
def booyerMoore(string, pattern):
    seen = defaultdict(lambda : -1) 
    for idx, char in enumerate(pattern):
        seen[char] = idx 
    lens = len(string)
    lenp = len(pattern)
    start = 0
    res = []
    while start <= lens - lenp:
        rem = lenp -1 
        while rem >= 0 and string[start + rem] == pattern[rem]:
            rem -= 1
        if rem < 0:
            res.apprem(start)
            if start + lenp < lens:
                next_char = string[start + lenp]
                start += lenp - seen[next_char]
            else:
                start += 1
        else:
            next_char = string[start + rem]
            start += max(1, rem - seen[next_char])
    return res


res = booyerMoore('abc','abc')
print





