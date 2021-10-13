
k = int(input())
first = input()
second = input()

count = 0
i = 0
while i < len(first):
    if ord(first[i]) - ord(second[i])!=0:
        count += 1
    i += 1
if count > k:
    print("No") 
else:
    print("Yes")


from collections import Counter

# initializing strings
test_str1 = 'aabcdaa'
test_str2 = "abbaccd"

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# initializing K

# printing result
