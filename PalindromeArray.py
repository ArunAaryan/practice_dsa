def isPalindrome(n):
    number = n
    reverse = 0
    while n:
        r = n % 10
        reverse = reverse * 10 + r
        n = n // 10
    print(reverse)
    if number == reverse:
        return True
    else:
        return False
        
def PalinArray(arr):
    res = 0
    for val in arr:
        if not isPalindrome(val):
            res += 1
    return res

print(isPalindrome(121))