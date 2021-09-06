arr = [2,3,8,5,7,4,1,2]
def findNumberOfHouses(arr, r, units):
    required = r * units
    food = 0
    if not units:
        return 0
    if not arr:
        return -1
    for i in range(len(arr)):
        food += arr[i]
        if food >= required:
            return i + 1
    if food != required:
        return 0
        
def findHouses(arr, r, units):
    required = r * units
    if not arr:
        return - 1
    for i in range(len(arr)):
        required -= arr[i] 
        if required <= 0:
            return i + 1
    return 0

# res = findNumberOfHouses(arr,7, 2)
res = findHouses(arr,7, 2)
print(res)

