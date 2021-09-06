def numbersInRange(left, right):
    if left >= right:
        return None 
    res = []
    for num in range(left, right + 1):
        if num % 7 == 0:
            res.append(num)
    return sum(res)
res = numbersInRange(1, 100)
print(res)
            

