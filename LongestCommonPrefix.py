from collections import deque
def longestCommonPrefix(strs):
        if not strs:
            return ""
        shortest = min(strs, key = len)
        for idx, char in enumerate(shortest):
            for value in strs:
                if char != value[idx]:
                    return shortest[:idx]
        return shortest


res = longestCommonPrefix( strs = ["flower","flow","flight"])
print(res)