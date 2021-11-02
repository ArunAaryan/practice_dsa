def printAllSubsequences(string):
    for l in range(1, len(string)+ 1):
        for start in range(len(string) - l + 1):
            print(string[start : start + l])
        
res = printAllSubsequences('abcd')


    
