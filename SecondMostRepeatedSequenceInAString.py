from heapq import heappush, heappop
from collections import defaultdict
def secondMostRepeated(arr):
    first_max = (1, arr[0])
    second_max = (1, arr[1]) 
    seen = defaultdict(lambda : 0) 
    seen[arr[0]] = 1
    seen[arr[1]] = 1
    for val in arr[2:]:
        seen[val] += 1 
        if seen[val] > first_max[0]:
            second_max = first_max
            first_max = (seen[val], val) 
        elif seen[val] > second_max[0] and seen[val] != first_max[0]:
            second_max = (seen[val], val)

    print(seen)
    print(first_max, second_max)
    return second_max[1]
res = secondMostRepeated(["geeks", "for", "geeks", "for", "geeks", "aaa"])
print(res)


