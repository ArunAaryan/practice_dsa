# online solution 
def wordBreak(words, word, lookup):
    # `n` stores length of the current substring
    n = len(word)
 
    # return true if the end of the string is reached
    if n == 0:
        return True
 
    # if the subproblem is seen for the first time
    if lookup[n] == -1:
 
        # mark subproblem as seen (0 initially assuming string
        # can't be segmented)
        lookup[n] = 0
 
        for i in range(1, n + 1):
            # consider all prefixes of the current string
            prefix = word[:i]
 
            # if the prefix is found in the dictionary, then recur for the suffix
            if prefix in words and wordBreak(words, word[i:], lookup):
                # return true if the string can be segmented
                lookup[n] = 1
                return True
 
    # return solution to the current subproblem
    return lookup[n] == 1
 
 
# Word Break Problem Implementation in Python
if __name__ == '__main__':
 
    # Set of strings to represent a dictionary
    # we can also use a Trie or a List to store a dictionary
    words = {
        'like', 'i'
    }
 
    # input string
    word = 'likei'
 
    # lookup table to store solutions to subproblems
    # lookup[i] stores if substring word[n-i…n) can be segmented or not
    lookup = [-1] * (len(word) + 1)
 
    if wordBreak(words, word, lookup):
        print('The string can be segmented')
    else:
        print('The string can\'t be segmented')

# neetcoder's solution 
def wordBreakNeet(s, dictionary):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    for i in range(len(s) - 1, -1, -1):
        for word in dictionary:
            if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                dp[i] = dp[i + len(word)]
            if dp[i]:
                break
    return dp[0]
res = wordBreakNeet(
    'neetcode',['neet', 'leet','code']
)
print(res) 