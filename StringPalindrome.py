def stringPalindrome(str):
    left = 0
    right = len(str) - 1
    while left <= right:
        if str[left] != str[right]:
            return 'Not palindrome'
        left += 1
        right -= 1
    return 'palindrome' 
str = 'paliioilap'
res = stringPalindrome(str) 
print(res)
