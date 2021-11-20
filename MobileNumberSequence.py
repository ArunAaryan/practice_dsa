def mobileNumberSequence(string):
    keypad = ["2", "22", "222", #a, b, c
       "3", "33", "333", # d e f
       "4", "44", "444", # g h i
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999" ]
    res = ''
    for char in string:
        if char == " " :
            res += '0'
        else:
            position = ord(char) - ord('a')
            res += keypad[position]
    return res


res = mobileNumberSequence('arun')
print(res)
